from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

CREATE_USER_URL = reverse('user:create')

def create_user(**param):
    return get_user_model().objects.create_user(**param)

# public test api

class PublicUserApiTest(TestCase):

    def set_up(self):
        self.client = APIClient()

    # "define playload"

    def test_create_valid_user_success(self):
        payload ={
            'email':'samkhan86@gmail.com',
            'password':'testpass',
            'username':'samkhan',
        }

        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user=get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn('password',res.data)

    def test_user_exist(self):
        payload ={'email':'samkhan86@gmail.com','password':'testpass'}
        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_to_short(self):
        payload ={'email':'samkhan86@gmail.com','password':'te'}
        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exist=get_user_model().objects.filter(
            email=payload["email"]
        ).exist()
        self.assertFalse(user_exist)




