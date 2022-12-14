# Generated by Django 4.0.3 on 2022-08-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0017_remove_productuploadmodel_product_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pro_image',
            field=models.ImageField(upload_to='product_image/'),
        ),
        migrations.AlterField(
            model_name='productuploadmodel',
            name='product_images1',
            field=models.ImageField(null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='productuploadmodel',
            name='product_images2',
            field=models.ImageField(null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='productuploadmodel',
            name='product_images3',
            field=models.ImageField(null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='productuploadmodel',
            name='product_images4',
            field=models.ImageField(null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='productuploadmodel',
            name='product_images5',
            field=models.ImageField(null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='sellerdetailsmodel',
            name='address_proof',
            field=models.ImageField(upload_to='addressproof/'),
        ),
        migrations.AlterField(
            model_name='sellerdetailsmodel',
            name='com_logo',
            field=models.ImageField(upload_to='companylogo/'),
        ),
        migrations.AlterField(
            model_name='sellerdetailsmodel',
            name='pancard',
            field=models.ImageField(upload_to='pancard/'),
        ),
    ]
