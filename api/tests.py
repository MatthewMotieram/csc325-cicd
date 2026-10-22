from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"status": "ok"})


class HelloEndpointTests(APITestCase):
    def test_hello_default_name(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Hello, World!")

    def test_hello_custom_name(self):
        response = self.client.get(reverse("hello"), {"name": "Ada"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Hello, Ada!")

    def test_hello_includes_course(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.json()["course"], "CSC325")

    def test_hello_includes_version(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.json()["version"], "1.1")
