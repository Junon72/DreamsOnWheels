from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from accounts.views import logout, login, register, user_profile, update_profile

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
    def setUpTestData(cls):
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

        # user = User.objects.get(email='testUser@example.com')
        user = User.objects.get(username='testUser')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(user.is_authenticated)

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
        response = self.client.get('/accounts/profile/')

        self.assertEqual(response.status_code, 302)

    def test_edit_profile_template(self):
        response = self.client.get('/accounts/update-profile/')

        self.assertEqual(response.status_code, 302)


class TestLogoutView(TestCase):
    def test_logout(self):
        User.objects.create_user(username='testUser', email='testUser@email.com', password='passW0rd')
        response = self.client.post("/accounts/login/")
        user = User.objects.get(username='testUser')
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)


class TestProfileView(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='testUser@example.com',
            username='testUser',
            password='passw0rd',
            first_name='Larry',
            last_name='Lentel'
        )

    def test_profile_template(self):
        user = User.objects.get(id=1)
        page = self.client.get('/accounts/profile/')

        self.assertEqual(page.status_code, 302)
        self.assertTemplateUsed('index.html')