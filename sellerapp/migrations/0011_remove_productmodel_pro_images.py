# Generated by Django 4.0.1 on 2022-05-11 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0010_productmodel_pro_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='Pro_images',
        ),
    ]
