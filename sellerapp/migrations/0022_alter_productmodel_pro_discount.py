# Generated by Django 4.0.3 on 2022-09-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0021_alter_productmodel_pro_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pro_discount',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]