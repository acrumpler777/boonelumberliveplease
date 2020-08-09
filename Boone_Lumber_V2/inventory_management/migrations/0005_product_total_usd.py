# Generated by Django 3.0.9 on 2020-08-05 22:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0004_product_bf_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Total_USD',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
    ]
