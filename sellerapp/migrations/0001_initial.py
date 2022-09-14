# Generated by Django 4.0.1 on 2022-04-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerDetailsModel',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_name', models.CharField(max_length=100)),
                ('own_name', models.CharField(max_length=100)),
                ('phno', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pancard', models.ImageField(upload_to='images/')),
                ('com_logo', models.ImageField(upload_to='images/')),
                ('address_proof', models.ImageField(upload_to='images/')),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]