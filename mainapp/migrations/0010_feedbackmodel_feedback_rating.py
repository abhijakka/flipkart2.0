# Generated by Django 4.0.3 on 2022-09-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_feedbackmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='feedback_rating',
            field=models.CharField(help_text='feedback_rating', max_length=200, null=True),
        ),
    ]
