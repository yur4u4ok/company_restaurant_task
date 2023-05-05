import pytest

from rest_framework.test import APIClient
from rest_framework import status

from apps.restaurant.models import RestaurantModel

client = APIClient()


@pytest.mark.django_db
def test_create_restaurant(client):
    prev_count = RestaurantModel.objects.count()
    sample_restaurant = {
        'restaurant_name': 'Emily'
    }

    response = client.post("restaurant", sample_restaurant)

    assert response.status_code, status.HTTP_201_CREATED
    assert RestaurantModel.objects.count() == prev_count + 1
