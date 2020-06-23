from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.views import logout, login, register, user_profile, update_profile
from django.contrib.messages import get_messages


class TestRegisterUserView(TestCase):

    def test_register_template(self):
        response = self.client.get('/accounts/register/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_invalid_form_does_not_register(self):
        response = self.client.post('/accounts/register/', {
        'username': 'testUser2',
        'email': 'testUser2@mail.com',
        'password1': 'Apassword1',
        'password2': 'Apassword1ss',
        })
        self.assertEqual(User.objects.count(), 0)

    def test_can_register_user(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post('/accounts/register/', {
            'username': 'testUser1',
            'email': 'testUser1@mail.com',
            'password1': 'Apassword1',
            'password2': 'Apassword1',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)


class TestLoginView(TestCase):

    @classmethod
    def setUp(cls):
        User.objects.create_user(
            email='testUser@example.com',
            username='testUser',
            password='passw0rd'
        )

    def test_get_login_template(self):
        response = self.client.get('/accounts/login/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_can_login_with_valid_credentials(self):
        """
        Credential validation test is performed separately with
        valid username and valid email
        """

        response = self.client.post("/accounts/login/")

        user = User.objects.get(username='testUser')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(user.is_authenticated)

        for message in get_messages(response.wsgi_request):
            self.assertEqual(message.tags, "success")
            self.assertTrue('You have successfully logged in!' in message.message)

    def test_response_not_valid_credentials(self):
        """
        FormErrorResponse test is performed with no credentials, 
        and false credentials
        """

        response = self.client.post("/accounts/login/", {
            'username': 'testUser',
            'password': 'pass0word'
        })
        # user = User.objects.get(email='testUser@example.com')
        user = User.objects.get(username='testUser')

        self.assertFormError(response, 'form', None,
                            'Your username or password is incorrect!')

    def test_get_profile_template(self):
        """
        Test logged in user can access profile page
        """
        response = self.client.get('/accounts/profile/')

        self.assertEqual(response.status_code, 302)

    def test_edit_profile_template(self):
        response = self.client.get('/accounts/update-profile/')

        self.assertEqual(response.status_code, 302)
        for message in get_messages(response.wsgi_request):
            self.assertEqual(message.tags, "success")
            self.assertTrue('Your profile has been updated successfully!' in message.message)


class TestLogoutView(TestCase):

    def test_logout(self):
        User.objects.create_user(username='testUser', email='testUser@email.com', password='passW0rd')
        self.client.login(username='testUser', password='passW0rd') 
        response = self.client.get("/accounts/logout/")

        self.assertEqual(response.status_code, 302)
        for message in get_messages(response.wsgi_request):
            self.assertEqual(message.tags, "success")
            self.assertTrue('You have successfully logged out!' in message.message)


class TestUpdateProfileView(TestCase):

    def test_profile(self):
        User.objects.create_user(username='testUser', email='testUser@email.com', password='passW0rd')
        self.client.login(username='testUser', password='passW0rd') 
        response = self.client.get("/accounts/profile/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('profile.html')
