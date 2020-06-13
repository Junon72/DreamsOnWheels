from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm


class TestUserLoginForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='testUser@example.com',
            username='testUser',
            password='passw0rd',
            first_name='Larry',
            last_name='Lentel'
        )

    def test_login_form_with_username_and_password(self):
        form = UserLoginForm({'username': 'testUser',
                              'password': 'passw0rd'})
        self.assertTrue(form.is_valid())

    def test_login_username_is_required(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_login_password_is_required(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
        

class TestUserRegistrationForm(TestCase):

    def test_registration_passwords_are_a_match(self):
        form = UserRegistrationForm({
            'username': 'testUser0',
            'email': 'testUser0@test.com',
            'password1': 'bigSecret0',
            'password2': 'bigSecret0',
            })
        self.assertTrue(form.is_valid())
        
    def test_registration_passwords_are_not_a_match(self):
        form = UserRegistrationForm({
            'username': 'testUser0',
            'email': 'testUser0@test.com',
            'password1': 'bigSecret0',
            'password2': 'bigSecret1',
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords do not match'])

    def test_registration_email_is_unique(self):
        User.objects.create_user(
            username='testUser1',
            email='testUser0@test.com'
        )
        form = UserRegistrationForm({
            'username': 'testUser0',
            'email': 'testUser0@test.com',
            'password1': 'bigSecret0',
            'password2': 'bigSecret0'
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'Email address must be unique.'])

    def test_username_field_is_required(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_password_field_is_required(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])

