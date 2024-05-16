import json
import pytest
from pages.pet_page import PetPage
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def pet_page():
    return PetPage()


@pytest.fixture
def create_pet(pet_page):
    with open('data/create_pet_data.json') as create_pet_data:
        pet_data = json.load(create_pet_data)

    response = pet_page.add_pet(pet_data)
    assert response.status_code == 200, f"Failed to create pet: {response.text}"

    pet_id = response.json()["id"]
    return pet_id
