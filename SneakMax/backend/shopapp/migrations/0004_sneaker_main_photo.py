# Generated by Django 5.1.2 on 2025-01-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_rename_country_sneaker_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='main_photo',
            field=models.ImageField(default='/default.jpg', upload_to='images/'),
        ),
    ]
