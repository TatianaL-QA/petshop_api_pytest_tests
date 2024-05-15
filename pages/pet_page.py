from utils.api_client import APIClient
from utils.constants import API_BASE_URL


class PetPage:
    def __init__(self):
        self.api_client = APIClient()
        self.response_code = None
        self.response_json = None

    def post_pet_image(self, pet_id, pet_img_path):
        endpoint = f"{API_BASE_URL}/pet/{pet_id}/uploadImage"
        with open(pet_img_path, 'rb') as image_file:
            files = {'file': (pet_img_path, image_file, 'image/png')}
            response = self.api_client.post(endpoint, files=files)
            self.response_code = response.status_code
            self.response_json = response.json()

    def get_pet_by_id(self, pet_id):
        endpoint = f"{API_BASE_URL}/pet/{pet_id}"
        response = self.api_client.get(endpoint)
        self.response_code = response.status_code
        self.response_json = response.json()

    def add_pet(self, pet_data):
        endpoint = f"{API_BASE_URL}/pet"
        response = self.api_client.post(endpoint, json=pet_data)
        self.response_code = response.status_code
        self.response_json = response.json()

    def update_pet(self, pet_data):
        endpoint = f"{API_BASE_URL}/pet/"
        response = self.api_client.put(endpoint, json=pet_data)
        self.response_code = response.status_code
        self.response_json = response.json()


# TODO methods for other endpoints (PUT, DELETE, etc.)
