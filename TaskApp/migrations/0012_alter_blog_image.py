# Generated by Django 4.2.4 on 2023-08-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0011_alter_blog_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile/'),
        ),
    ]