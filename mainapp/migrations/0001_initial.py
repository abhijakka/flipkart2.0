# Generated by Django 4.0.3 on 2022-09-02 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellerapp', '0019_productuploadmodel_product_watchlist'),
        ('userapp', '0002_alter_userdetailsmodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_product_qty', models.CharField(help_text='product_quantity', max_length=50, null=True)),
                ('cart_product_price', models.CharField(help_text='Prodcuts_price', max_length=50, null=True)),
                ('cart_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetailsmodel')),
                ('cart_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sellerapp.productuploadmodel')),
            ],
            options={
                'db_table': 'cart_details',
            },
        ),
    ]
