# Generated by Django 4.0.1 on 2022-04-18 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0004_productuploadmodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productuploadmodel',
            table='product_photos_details',
        ),
    ]
