# Generated by Django 5.1 on 2024-08-22 19:41

import productos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[productos.models.validate_precio]),
        ),
    ]
