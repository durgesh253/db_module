# Generated by Django 5.0 on 2023-12-26 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_model', models.CharField(max_length=200)),
                ('product_ram', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]