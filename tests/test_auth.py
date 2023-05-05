import pytest

from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_employee(client):
    payload = dict(
        email='user@gmail.com',
        password='user',
        profile=dict(
            name="Ostap",
            surname="Yurchuk",
            age=20
        )
    )

    response = client.post("auth/register", payload, format='json')

    data = response.data

    assert data["email"] == payload["email"]


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post("auth", dict(email="user@gmail.com", password="qwerty"))

    assert response.status_code == 404

