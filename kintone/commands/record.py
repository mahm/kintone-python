class Record:
    def __init__(self, http_request):
        self.http_request = http_request
        self.path = f'/k/v1/record.json'

    def get(self, app_id: int, record_id: int) -> dict:
        params = {'app': app_id, 'id': record_id}
        return self.http_request.get(self.path, params)

    def create(self, app_id: int, record: dict) -> dict:
        params = {'app': app_id, 'record': record}
        return self.http_request.post(self.path, params)

    register = create  # alias method

    def update(self, app_id: int, record_id: int, record: dict) -> dict:
        params = {'app': app_id, 'id': record_id, 'record': record}
        return self.http_request.put(self.path, params)
