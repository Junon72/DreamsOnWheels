from unittest import mock
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import SimpleTestCase, TestCase, override_settings, Client


@override_settings(ROOT_URLCONF='project.urls')
class TestCustomErrorHandlers(SimpleTestCase):

    def test_handler_renders_template_response_404(self):
        response = self.client.get('/404/')
        self.assertContains(response, 'Oops! Nothing to see here.', status_code=404)


class TestErrors(TestCase):
    """Test Error handling"""

    @classmethod
    def setUpClass(cls):
        super(TestErrors, cls).setUpClass()
        cls.username = 'admin'
        cls.email = 'admin@localhost'
        cls.password = 'testpassword123'
        cls.not_found_url = '/i-do-not-exist/'
        cls.internal_server_error_url = reverse('password_reset')

    def setUp(self):
        super(TestErrors, self).setUp()
        User = get_user_model()

        User.objects.create_user(
            self.username,
            self.email,
            self.password,
            is_staff=True,
            is_active=True
        )
        self.client = Client(raise_request_exception=False)

    # Mock in order to trigger Exception and resulting Internal server error
    @mock.patch('django.contrib.auth.views.PasswordResetView.form_class', None)
    @override_settings(DEBUG=False)
    def test_errors(self):
        self.client.login(username=self.username, password=self.password)

        with self.subTest("Not found (404)"):
            response = self.client.get(self.not_found_url, follow=True)
            self.assertNotIn('admin/', str(response.content))

        with self.subTest("Internal server error (500)"):
            response = self.client.get(self.internal_server_error_url,
                                       follow=True)
            self.assertNotIn('TypeError', str(response.content))
