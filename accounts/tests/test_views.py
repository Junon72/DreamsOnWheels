from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404


class TestLoginView(TestCase):

    def test_get_login_form(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_can_log_in(self):
        user1 = User.objects.create_user(
            username='testUser',
            email='testUser@example.com',
            password='passw0rd')

        response = self.client.get('/events/')
        self.assertEqual(response.context['user'], AnonymousUser())

        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'pass0word'
        })

        response = self.client.get('/accounts/login')

    def test_user_does_not_exist(self):
        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'pass0word'
        })
        self.assertFormError(response, 'form', None, 'Your username or password is incorrect!', ' ')


class TestRegisterUserView(TestCase):
    def test_get_register_user_form(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_can_register_user(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post("/accounts/register", {
            'username': 'testUser1',
            'email': 'testUser1@mail.com',
            'password1': 'Apassword1',
            'password2': 'Apassword1',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/index/')
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_form_does_not_register(self):
        response = self.client.post("/accounts/register/", {
            'username': 'testUser2',
            'email': 'testUser2@mail.com',
            'password1': 'Apassword1',
            'password2': 'Apassword1ss',
        })
        self.assertEqual(User.objects.count(), 0)


class TestLogoutView(TestCase):
    def test_logout(self):
        response = self.client.get("/accounts/logout")
        print(response)
        self.assertRedirects(response, '/index/')
        self.assertEqual(response, )