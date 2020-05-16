from django.db import models



STATUS_CHOICES = [
    ('d', 'Draft'),
    ('h', 'Highlight'),
    ('a', 'Active'),
    ('i', 'Inactive')
]


class Original(models.Model):
    make = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=300, default='')
    description = models.TextField()
    build_year = models.PositiveIntegerField(default='')
    image_main = models.ImageField(upload_to="original_images")
    image_two = models.ImageField(upload_to="original_images", blank=True)
    image_three = models.ImageField(upload_to="original_images", blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    votes = models.PositiveIntegerField(default='0')
    price_min = models.DecimalField(max_digits=16, decimal_places=2, blank=True)
    price_max = models.DecimalField(max_digits=16, decimal_places=2, blank=True)


    def __str__(self):
        return self.model


PRODUCT_STATUS_CHOICES = [
    ('p', 'Promotion'),
    ('s', 'Soldout'),
    ('o', 'Out of stock'),
    ('n', 'Not on sales'),
    ('y', 'On sales')
]

class Product(models.Model):
    make = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=300, default='')
    description = models.TextField()
    scale = models.CharField(max_length=60, default='')
    manufacturer = models.CharField(max_length=200, default='')
    build_year = models.PositiveIntegerField(default='0')
    color = models.CharField(max_length=30, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default='0.0')
    image_main = models.ImageField(upload_to="product_images")
    image_sec = models.ImageField(upload_to="product_images", blank=True)
    status = models.CharField(max_length=1, choices=PRODUCT_STATUS_CHOICES, default='y')
    in_stock = models.PositiveIntegerField(default='0')
    original_key = models.ForeignKey(Original, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.model



