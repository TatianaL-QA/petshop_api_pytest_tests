import requests


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.default_headers = {'Content-Type': 'application/json'}

    def get(self, url, **kwargs):
        print(f"Sending GET request to: {url}")
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, files=None, headers=None, **kwargs):
        print(f"Sending POST request to: {url}")
        merged_headers = {**self.default_headers, **(headers or {})}  # Merge default and custom headers
        if files:  # Check if multipart request
            merged_headers['Content-Type'] = 'multipart/form-data'  # Override content type for multipart request
        return self.session.post(url, data=data, files=files, headers=merged_headers, **kwargs)

    def put(self, url, data=None, files=None, headers=None, **kwargs):
        print(f"Sending PUT request to: {url}")
        merged_headers = {**self.default_headers, **(headers or {})}  # Merge default and custom headers
        if files:  # Check if multipart request
            merged_headers['Content-Type'] = 'multipart/form-data'  # Override content type for multipart request
        return self.session.put(url, data=data, files=files, headers=merged_headers, **kwargs)

    def delete(self, url, **kwargs):
        print(f"Sending DELETE request to: {url}")
        return self.session.delete(url, **kwargs)

# TODO add other HTTP methods
