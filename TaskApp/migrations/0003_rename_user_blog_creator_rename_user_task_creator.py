# Generated by Django 4.2.4 on 2023-08-10 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0002_task_updated_at_task_user_alter_task_created_at_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='creator',
        ),
    ]
