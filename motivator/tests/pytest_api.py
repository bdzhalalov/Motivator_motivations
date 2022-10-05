import pytest


@pytest.mark.django_db
def test_models(motivation):
    test_motivation = motivation
    assert test_motivation.nickname == 'test_user'


@pytest.mark.django_db
def test_get(client):
    response = client.get('/motivations/')
    assert response.status_code == 200
    assert len(response.data['results']) == 1

@pytest.mark.django_db
def test_permissions():
    pass