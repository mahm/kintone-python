class App:
    def __init__(self, http_request):
        self.http_request = http_request

    def get(self, app_id: int) -> dict:
        path = f'/k/v1/app.json'
        params = {'id': app_id}
        return self.http_request.get(path, params)
