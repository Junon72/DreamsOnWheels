from django.test import TestCase
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, AnonymousUser
from .views import *


class TestAccountsLoginViews(TestCase):
    
    def test_login_url_exists_at_accounts(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        
    def test_login_url_is_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_uses_login_form_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def UserLoginCase(self):
        """ 
        Test if user can log in
        """
        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret0'}
            User.objects.create(**self.credentials)
        
        def test_user_can_login(self):
            # after login access user profile requiring login
            response = self.client.post('/user/profile/', self.credentials, follow=True)
            # check if user is authenticated
            self.assertTrue(response.context['user'].is_authenticated)
            self.assertEqual(response.context['user'].AnonymousUser())
            response = self.client.get('/accounts/login')
            
    # def test_user_does_not_exist(self):
    #     response = self.client.post("/accounts/login", {
    #         'username': 'testuser',
    #         'password': 'secret0'
    #     })
    #     self.assertFormError(response.context['user'], None, 'Incorrect Username or Password!')
            
            
class TestAccountsRegisterUserViews(TestCase):
    
    def test_register_url_exists_at_accounts(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        
    def test_register_url_is_accessible_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_uses_register_form_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_not_valid_form_rejected(self):
        response = self.client.post('/accounts/register/', {
            'username': 'testUser0',
            'email': 'testUser0@test.com',
            'password1': 'bigSecret0',
            'password2': 'bigSecret1',
            })
        self.assertEqual(User.objects.count(), 0)

    def test_can_register_new_user(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post('/accounts/register/', {
            'username': 'testUser0',
            'email': 'testUser0@test.com',
            'password1': 'bigSecret0',
            'password2': 'bigSecret0',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'index')
        self.assertEqual(User.objects.count(), 1)
        
class TestAccountsUserLogout(TestCase):
    def test_logout_route(self):
        response = self.client.get('/accounts/logout')
        self.assertRedirects(response, 'index')