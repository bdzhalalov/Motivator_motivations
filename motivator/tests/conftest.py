import pytest
from motivations.models import Motivation
from rest_framework.test import APIClient
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def motivation():
    motivation = Motivation.objects.create(
        nickname = 'test_user',
        motivation = 'Test motivation'
    )

    return motivation


@pytest.fixture
def client():
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION =os.getenv('API_KEY')
    )
    return client

