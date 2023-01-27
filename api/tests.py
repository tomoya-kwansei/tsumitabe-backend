import json

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
    def setUp(self):
        UserFactory.create_batch(50, email=factory.Sequence(lambda n: 'testemail%d@example.com' % n))

    def test_access_from_not_authenticated_user(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 401)

    def test_access_from_authenticated_user(self):
        user = UserFactory.create()
        self.client.force_authenticate(user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)


class AuthenticateViewTest(APITestCase):
    def test_get_by_not_authenticated_user(self):
        response = self.client.get('/api/login/')
        self.assertEqual(response.status_code, 401)

    def test_get_by_authenticated_user(self):
        PASSWORD = "aaaaaaa"
        user = UserFactory.create()
        user.set_password(PASSWORD)
        user.save()
        self.client.login(email=user.email, password=PASSWORD)
        response = self.client.get('/api/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_by_not_authenticated_user(self):
        PASSWORD = "aaaaaaa"
        user = UserFactory.create()
        user.set_password(PASSWORD)
        user.save()
        response = self.client.post('/api/login/', 
        data=json.dumps({
            "email": user.email,
            "password": PASSWORD
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
