import pytest
from pages.pet_page import PetPage
import json

pytestmark = [pytest.mark.positive_test]


@pytest.fixture
def pet_page():
    return PetPage()


def test_add_pet(pet_page):
    pet_data = {
        "id": 1,
        "name": "Fluffy",
        "status": "available"
    }
    pet_page.add_pet(pet_data)

    assert pet_page.response_code == 200
    assert pet_page.response_json["name"] == pet_data["name"]


def test_get_pet_by_id(pet_page):
    pet_id = 1
    pet_page.get_pet_by_id(pet_id)

    assert pet_page.response_code == 200
    assert pet_page.response_json["name"] == "Fluffy"


def test_update_pet(pet_page):

    with open('./data/update_pet_data.json') as json_file:
        update_pet_data = json.load(json_file)

    pet_page.update_pet(update_pet_data)

    assert pet_page.response_code == 200, f"Expected response code: 200, Actual response code: {pet_page.response_code}"
    assert pet_page.response_json["name"] == "doggie"


def test_upload_image(pet_page):
    pet_id = 1
    pet_img_path = "./data/doggo.png"
    pet_page.post_pet_image(pet_id=pet_id, pet_img_path=pet_img_path)

    assert pet_page.response_code == 200, f"Expected response code: 200, Actual response code: {pet_page.response_code}"
    # Check if the response message indicates successful upload
    assert "File uploaded" in pet_page.response_message, "Upload went wrong"
