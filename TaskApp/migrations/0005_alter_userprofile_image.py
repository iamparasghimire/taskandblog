# Generated by Django 4.2.4 on 2023-08-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
