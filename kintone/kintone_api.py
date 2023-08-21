import base64
import urllib3

class KintoneApi:
    def __init__(self, domain: str, user: str, password: str = None, api_token: str = None) -> None:
        self.url_prefix = f"https://{domain}"
        self.user = user
        self.password = password
        self.api_token = api_token
        self.http = urllib3.PoolManager()

    def _build_headers(self, user: str = None, password: str = None, api_token: str = None) -> dict:
        if api_token:
            return {'Authorization': f'Bearer {api_token}'}
        else:
            credentials = f'{user}:{password or ""}'
            return {'Authorization': 'Basic ' + base64.b64encode(credentials.encode()).decode()}

    def get(self, path: str, headers: dict = None, params: dict = None):
        response = self.http.request('GET', self.url_prefix + path, headers=headers, fields=params)
        return {'message': 'success'}

    def post(self, path: str, headers: dict = None, body: dict = None):
        response = self.http.request('POST', self.url_prefix + path, headers=headers, body=body)
        return {'message': 'success'}

    def delete(self, path: str, headers: dict = None, params: dict = None):
        response = self.http.request('DELETE', self.url_prefix + path, headers=headers, fields=params)
        return {'message': 'success'}

    def post_file(self, path: str, headers: dict = None, file_path: str = None):
        with open(file_path, 'rb') as file:
            response = self.http.request('POST', self.url_prefix + path, headers=headers, body=file)
        return {'message': 'success'}
