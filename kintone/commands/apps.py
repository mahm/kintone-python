class Apps:
    def __init__(self, http_request):
        self.http_request = http_request


    def get(self, ids: list = None, codes: list = None, name: str = None, space_ids: list = None, offset: int = None, limit: int = None) -> dict:
        path = f'/k/v1/apps.json'
        params = {
            'ids': ids,
            'codes': codes,
            'name': name,
            'spaceIds': space_ids,
            'offset': offset,
            'limit': limit
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self.http_request.get(path, params)
