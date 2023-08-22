import base64
import urllib3
import json
from typing import Union, List


class HttpRequest:
    def __init__(self, domain: str, user: str = None, password: str = None,
                 token: Union[str, List[str]] = None) -> None:
        self.url_prefix = f"https://{domain}"
        self.user = user
        self.password = password
        if token:
            self.token = token if isinstance(token, str) else ','.join(token)
        else:
            self.token = None
        self.http = urllib3.PoolManager()

    def _build_headers(self) -> dict:
        headers = {}
        if self.token:
            headers['X-Cybozu-API-Token'] = f'{self.token}'
        elif self.user:
            credentials = f'{self.user}:{self.password or ""}'
            headers['X-Cybozu-Authorization'] = base64.b64encode(credentials.encode()).decode()
        else:
            raise ValueError("Either user and password or token must be provided.")
        headers['Content-Type'] = 'application/json'
        return headers

    def get(self, path: str, params: dict = None):
        headers = self._build_headers()
        response = self.http.request('GET', self.url_prefix + path, headers=headers, fields=params)
        result = json.loads(response.data.decode('utf-8'))
        return result

    def post(self, path: str, body: dict = None):
        headers = self._build_headers()
        body = bytes(json.dumps(body), encoding="utf-8")
        response = self.http.request('POST', self.url_prefix + path, headers=headers, body=body)
        result = json.loads(response.data.decode('utf-8'))
        return result

    def delete(self, path: str, params: dict = None):
        headers = self._build_headers()
        response = self.http.request('DELETE', self.url_prefix + path, headers=headers, fields=params)
        result = json.loads(response.data.decode('utf-8'))
        return result

    def post_file(self, path: str, file_path: str = None):
        headers = self._build_headers()
        with open(file_path, 'rb') as file:
            file_content = file.read()
            response = self.http.request('POST', self.url_prefix + path, headers=headers, body=file_content)
        result = json.loads(response.data.decode('utf-8'))
        return result
