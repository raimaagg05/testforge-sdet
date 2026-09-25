import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", timeout=10, **kwargs)

    def post(self, endpoint, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", timeout=10, **kwargs)
