import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from UserProfileAPI.models import User


class UserProfileTestCases(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.user_details = {
            "name": "Nick Fury",
            "email": "nick.fury@test.io",
            "phone_no": 9761254324,
            "password": "nickf12345",
            "gender": "Male"
        }
        cls.user_details_updated = {
            "name": "Nick Fury",
            "email": "nick.fury@test.io",
            "phone_no": 5432497612,
            "password": "nickf12345",
            "gender": "Male"
        }
        cls.user_details_2 = {
            "name": "Tony Stark",
            "email": "tony.stark@test.io",
            "phone_no": 9761324324,
            "password": "tonys12345",
            "gender": "Male"
        }
        cls.login_dict = {
            'email': "nick.fury@test.io",
            'password': "nickf12345"
        }
        cls.incorrect_login_dict = {
            'email': "nick.fury@test.io",
            'password': "12345nickf"
        }
        cls.invalid_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyZjViN2ZlYi01ZDQwLTRiZjgtYTdjZi1hZGJmNTQ4NjUzM2IiLCJ0aW1lIjoiMTAvMjAvMjAyMSwgMTA6NDY6NTEifQ.MhJpWV8wJP5lOVpnT_cSybCfDmQf7ERcbyW0ylpWoEY"
        cls.client.post(reverse("user-create"), cls.user_details, format='json')

    def test_correct_1_create_user(self):
        response = self.client.post(reverse("user-create"), self.user_details_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_incorrect_1_create_user(self):
        response = self.client.post(reverse("user-create"), self.user_details, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.all().count(), 1)

    def test_correct_2_login(self):
        response = self.client.post(reverse("user-login"), self.login_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual("token" in response_data, True)
        self.token = response_data["token"]

    def test_incorrect_2_login(self):
        response = self.client.post(reverse("user-login"), self.incorrect_login_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_correct_3_get_user(self):
        token = self.get_token(self.login_dict)
        response = self.client.get(reverse("user-details"), HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual("IP Address" in response_data, True)

    def test_correct_4_update_user(self):
        token = self.get_token(self.login_dict)
        response = self.client.put(reverse("user-details"), self.user_details_updated, format='json',
                                   HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual("IP Address" in response_data, True)

    def test_incorrect_5_delete_user(self):
        token = self.invalid_token
        response = self.client.delete(reverse("user-details"), HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(User.objects.all().count(), 1)

    def test_correct_5_delete_user(self):
        token = self.get_token(self.login_dict)
        response = self.client.delete(reverse("user-details"), HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)

    def get_token(self, login_dict):
        login_response = self.client.post(reverse("user-login"), login_dict, format='json')
        login_response_data = json.loads(login_response.content)
        return login_response_data["token"]
