# Generated by Django 4.1 on 2022-09-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_login_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Enter Date'),
        ),
    ]
