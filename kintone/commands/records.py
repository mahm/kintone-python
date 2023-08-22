class Records:
    def __init__(self, http_request):
        self.http_request = http_request
        self.path = f'/k/v1/records.json'

    def get(self, app_id: int, query: str = None, fields: list = None, total_count: bool = False) -> dict:
        params = {'app': app_id}
        if query:
            params['query'] = query
        if fields:
            params['fields'] = fields
        params['totalCount'] = 'true' if total_count else 'false'
        return self.http_request.get(self.path, params)

    def create(self, app_id: int, records: list) -> dict:
        params = {'app': app_id, 'records': records}
        return self.http_request.post(self.path, params)

    register = create  # alias method

    def update(self, app_id: int, records: list) -> dict:
        params = {'app': app_id, 'records': records}
        return self.http_request.put(self.path, params)

    def delete(self, app_id: int, ids: list, revisions: list = None) -> dict:
        params = {'app': app_id, 'ids': ids}
        if revisions:
            params['revisions'] = revisions
        return self.http_request.delete(self.path, params)
