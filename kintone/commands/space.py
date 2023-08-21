class Space:
    def __init__(self, http_request):
        self.http_request = http_request

    def get(self, space_id: int) -> dict:
        path = f'/k/v1/space.json'
        params = {'id': space_id}
        return self.http_request.get(path, params)
