# Generated by Django 4.2.6 on 2023-11-11 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_user_password1_user_password2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]
