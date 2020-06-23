from django.db import models
from django_countries.fields import CountryField
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = CountryField()
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} by {self.full_name} / {self.email}"


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        on_delete=models.CASCADE,
        related_name="lineitems"
    )
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.quantity} / {self.product.make} / {self.product.model} / € {self.product.price}"
