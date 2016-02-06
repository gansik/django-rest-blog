from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model, authenticate

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import RestEmailUser

class AccountTests(APITestCase):

    _user_model = get_user_model()

    _data = {
		'name': 'John Doe',
		'email': 'test@example.com',
		'password': 'qwerty',
    }

    def test_user_register(self):

        response = self.client.post(reverse('user-register'), self._data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self._user_model.objects.count(), 1)
        self.assertEqual(self._user_model.objects.get().email, self._data['email'])

    def test_user_get_token(self):

        self.test_user_register()	# register new user

        response = self.client.post(reverse('user-token'), self._data, format='json')

        token = str(Token.objects.get())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], token)

        return response.data['token']
