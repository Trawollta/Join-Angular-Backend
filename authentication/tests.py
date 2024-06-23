from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewTests(APITestCase):
    def setUp(self):
        # Erstellen eines Benutzers für die Authentifizierung
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

    def test_registration(self):
        """
        Testet die Registrierung eines neuen Benutzers.
        """
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list_authenticated(self):
        """
        Testet, ob die Benutzerliste für authentifizierte Benutzer zugänglich ist.
        """
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_unauthenticated(self):
        """
        Testet, ob die Benutzerliste für nicht authentifizierte Benutzer unzugänglich ist.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_current_user(self):
        """
        Testet, ob der aktuelle Benutzer korrekt abgerufen wird.
        """
        response = self.client.get(reverse('current_user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_logout(self):
        """
        Testet den Logout-Prozess.
        """
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
