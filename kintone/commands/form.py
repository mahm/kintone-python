class Form:
    def __init__(self, http_request):
        self.http_request = http_request

    def get(self, app_id: int) -> dict:
        path = f'/k/v1/form.json'
        params = {'app': app_id}
        return self.http_request.get(path, params)
