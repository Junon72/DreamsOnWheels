# Generated by Django 3.0.6 on 2020-05-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='original_images'),
        ),
        migrations.AlterField(
            model_name='original',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='original_images'),
        ),
        migrations.AlterField(
            model_name='original',
            name='price_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='original',
            name='price_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_sec',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='promo_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
