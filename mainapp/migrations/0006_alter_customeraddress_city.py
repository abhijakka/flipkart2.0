# Generated by Django 4.0.3 on 2022-09-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_customeraddress_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
