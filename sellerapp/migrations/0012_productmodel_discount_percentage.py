# Generated by Django 4.0.3 on 2022-08-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0011_remove_productmodel_pro_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='discount_percentage',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
