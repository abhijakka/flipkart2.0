# Generated by Django 4.0.3 on 2022-08-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0013_alter_productmodel_seller_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='Product_uploaded_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
