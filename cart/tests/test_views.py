from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.urls import reverse


class TestCartViews(TestCase):

    def test_get_add_product_to_cart(self):
        User.objects.create_user(
            email='testUser@example.com',
            username='testUser',
            password='passw0rd')
        self.client.login(username='testUser', password='passw0rd')
        product = Product.objects.create(make='Test Product',
                                         description='Some content',
                                         price='99.00', image_main='testproduct.jpg')

        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))

        session = self.client.session
        session['cart'] = 'cart_session'

        response = self.client.post("/cart/",
                                    kwargs={'product_id': product.id})
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)

    def test_get_delete_item_from_cart(self):
        User.objects.create_user(
            email='testUser@example.com',
            username='testUser',
            password='passw0rd')
        self.client.login(username='testUser', password='passw0rd')
        product = Product.objects.create(make='Test Product',
                                         description='Some content',
                                         price='99.00', image_main='testproduct.jpg')

        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))
        page = self.client.get("/cart/")

        session = self.client.session
        session["cart"] = "cart_session"

        quantity = 5
        response = self.client.post("/cart/",
                                    kwargs={"product_id": product.id},
                                    data={"quantity": quantity},
                                    follow=True)

        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)

        delete_item = self.client.post("/cart/",
                                       kwargs={"product_id": product.id},
                                       data={"quantity": (quantity - 1)},
                                       follow=True)

        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")