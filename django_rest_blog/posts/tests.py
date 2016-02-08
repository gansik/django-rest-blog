from django.core.urlresolvers import reverse
from django.test.client import RequestFactory

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

class PostsTests(APITestCase):

    _user_data = {
		'name': 'John Doe',
		'email': 'test@example.com',
		'password': 'qwerty',
    }

    def test_posts(self):
        # create new user
        self.client.post(reverse('user-register'), self._user_data, format='json')

        # get user token
        response = self.client.post(reverse('user-token'), self._user_data, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        # create new post
        self.client.post(reverse('post-list'), {
		'title': 'Hello World',
		'bodytext': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim...',
        }, format='json')


        # created successfully?
        response = self.client.get(reverse('post-detail', kwargs={'pk': 1}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug'], 'hello-world')

        # get posts list
        response = self.client.get(reverse('post-list'), format='json')
        self.assertEqual(response.data['count'], 1)

    def test_access(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('post-my'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.get(reverse('post-detail', kwargs={'pk': 0}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

