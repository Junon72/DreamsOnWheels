# Generated by Django 3.0.6 on 2020-05-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200517_1515'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='vote',
            name='unique vote',
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('user', 'highlight'), name='up_vote'),
        ),
    ]
