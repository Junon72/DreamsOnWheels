# Generated by Django 3.0.6 on 2020-06-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('n', 'New'), ('r', 'Sales read'), ('f', 'Sales follow'), ('d', 'Sales done'), ('c', 'Contributor request'), ('e', 'Contributor in exchange'), ('a', 'Contributor done'), ('or', 'Other read'), ('of', 'Other follow'), ('od', 'Other done')], default='n', max_length=2),
        ),
    ]
