# Generated by Django 4.0.3 on 2022-09-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_userdetailsmodel_customer_cart_address'),
        ('sellerapp', '0022_alter_productmodel_pro_discount'),
        ('mainapp', '0008_ordersmodels_order_product2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_message', models.CharField(help_text='feedback_message', max_length=200)),
                ('feedback_sentiment', models.CharField(help_text='sentiment_analysis', max_length=20, null=True)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('feedback_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetailsmodel')),
                ('feedback_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellerapp.productuploadmodel')),
                ('feedback_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellerapp.sellerdetailsmodel')),
            ],
            options={
                'db_table': 'feedback_details',
            },
        ),
    ]
