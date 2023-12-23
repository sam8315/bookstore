from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class SignUpPageTests(TestCase):
    username = 'hadi'
    email = 'hadi@gmail.com'

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEquals(response.status_code, 200)

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
        )
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.first().username, self.username),
        self.assertEqual(get_user_model().objects.first().email, self.email)
