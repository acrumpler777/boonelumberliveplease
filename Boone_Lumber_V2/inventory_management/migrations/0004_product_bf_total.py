# Generated by Django 3.0.9 on 2020-08-05 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_auto_20200805_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bF_Total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
    ]
