from utils.api_client import APIClient


class StorePage:
    def __init__(self):
        self.api_client = APIClient()
        self.response_code = None
        self.response_json = None