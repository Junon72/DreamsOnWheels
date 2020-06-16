from django.test import TestCase
from products.models import Product, Original


class TestProductViews(TestCase):

    def setUp(self):
        Product.objects.create(
            make='Test Make',
            model='Test Model',
            description='Test product description',
            scale='1:3',
            manufacturer='C.A.R.S.',
            build_year='1967',
            price=99.99,
            image_main='main.jpg',
            status='y',
        )
        Original.objects.create(
            make='Test Make',
            model='Test Model',
            description='Test product description',
            image_main='main.jpg',
            status='a',
            votes=0
        )

    def test_get_all_products_template(self):
        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('products.html')

    def test_get_original_template(self):
        original = Original.objects.get(id=1)
        response = self.client.get('/original/{0}'.format(original.id))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(original.make, 'Test Make')
        self.assertTemplateUsed('original.html')
