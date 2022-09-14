# Generated by Django 4.0.1 on 2022-04-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetailsModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.BigIntegerField()),
                ('profile_photo', models.ImageField(upload_to='images/')),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]