from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate

from .serializers import *
from .factories import *

class UserSerializerTests(TestCase):
    def test_create_valid_user(self):
        user_data = UserFactory.build()
        user_json = UserSerializer(user_data).data
        ser = UserSerializer(data=user_json)
        self.assertTrue(ser.is_valid())

    def test_create_user_with_invalid_email(self):
        user_data = UserFactory.build()
        user_data.email = "aaaaaaaaa"
        user_json = UserSerializer(user_data).data
        ser = UserSerializer(data=user_json)
        self.assertFalse(ser.is_valid())
        self.assertTrue("email" in ser.errors)

    # def test_create_user_with_empty_password(self):
    #     user_data = UserFactory.build()
    #     user_data.password = ""
    #     user_json = UserSerializer(user_data).data
    #     ser = UserSerializer(data=user_json)
    #     self.assertFalse(ser.is_valid())
    #     self.assertTrue("password" in ser.errors)


class UserViewSetTests(APITestCase):
    def test_access_from_not_authenticated_user(self):
        response = self.client.get('/api/users/')
        self.assertEqual(200, response.status_code)

    def test_access_from_authenticated_user(self):
        user = UserFactory.create()
        self.client.force_authenticate(user)
        response = self.client.get('/api/users/')
        self.assertEqual(200, response.status_code)
