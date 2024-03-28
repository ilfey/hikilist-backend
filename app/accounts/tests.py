from django.urls import path, include, reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from . import models

# Create your tests here.

class BaseTestCase(APITestCase):
    user = {
        "username": "test_user",
        "password": "test_user",
    }

    user_non_exists = {
        "username": "test_user123",
        "password": "test_user123",
    }


    def setUp(self):
        self.user_instance = models.User.objects.create_user(**self.user)


class RegisterViewTestCase(BaseTestCase):
    url = reverse('auth-register')
    

    def test_valid(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.post(self.url, self.user_non_exists)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_username_conflict(self):
        """
        Test to verify that a post call with already exists username
        """
        response = self.client.post(self.url, self.user)

        # Check the status code 
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

class LoginViewTestCase(BaseTestCase):
    url = reverse("auth-login")


    def test_valid(self):
        """
        Ensure we can login to the account.
        """
        response = self.client.post(self.url, self.user)

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_without_password(self):
        """
        Test to verify that can't login without password
        """
        response = self.client.post(self.url, {
            "username": self.user["username"]
        })

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_with_wrong_password(self):
        """
        Test to verify that can't login with wrong password.
        """
        response = self.client.post(self.url, {
            "username": self.user["username"],
            "password": "wrong_password",
        })

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LogoutViewTestCase(BaseTestCase):
    url = reverse("auth-logout")

    def setUp(self):
        super().setUp()

        self.refresh = RefreshToken.for_user(self.user_instance)
    
    def test_valid(self):
        """
        Ensure we can logout.
        """
        response = self.client.post(self.url, {
            "refresh": str(self.refresh)
        })

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_token(self):
        """
        Test to verify that can't logout with invalid refresh token.
        """
        response = self.client.post(self.url, {
            "refresh": "ivalid_token",
        })

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)