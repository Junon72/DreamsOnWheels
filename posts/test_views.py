from django.test import TestCase


def test_update_comment(self):
    comment = Comment.object.create(content='Test update commen')
    response = self.client.get(f'/update/(comment.pk)')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUser(response, "posts/")