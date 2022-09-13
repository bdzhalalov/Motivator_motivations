from rest_framework.test import APITestCase
from motivations.models import Motivation
from motivations.serializers import MotivationSerializer
from django.urls import reverse
from rest_framework import status
import unittest.mock
import os

class MotivationApiTestCase(APITestCase):

    @unittest.mock.patch.dict('os.environ', {'API-KEY': 'Test_value'})
    #TODO: Should make .env-testing file for test variables like API-KEY.
    def setUp(self):
        self.motivation = Motivation.objects.create(nickname='Test_user', motivation='Test motivation')

    def test_permissions(self):
        url = reverse('motivation-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get(self):
        url = reverse('motivation-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=os.getenv('API_KEY'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = reverse('motivation-list')
        data = {
            'nickname': 'Test_user',
            'motivation': 'Test motivation',
        }
        response = self.client.post(url, data=data, format="json", HTTP_AUTHORIZATION=os.getenv('API_KEY'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        url = reverse('motivation-detail', kwargs={'pk':self.motivation.pk})
        response = self.client.get(url, HTTP_AUTHORIZATION=os.getenv('API_KEY'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_detail(self):
        url = reverse('motivation-detail', kwargs={'pk':self.motivation.pk})
        data = {
            'nickname': 'Test_user',
            'motivation': 'Another test motivation',
            'is_visible': False
        }
        response = self.client.put(url, data=data, HTTP_AUTHORIZATION=os.getenv('API_KEY'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_detail(self):
        url = reverse('motivation-detail', kwargs={'pk':self.motivation.pk})
        response = self.client.delete(url, HTTP_AUTHORIZATION=os.getenv('API_KEY'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_motivation_serializer(self):
        serializer_data = MotivationSerializer(self.motivation).data
        expected_data = {
            'id': self.motivation.id,
            'nickname': 'Test_user',
            'motivation': 'Test motivation', 
            'is_visible': True
        }
        self.assertEqual(expected_data, serializer_data)