# Generated by Django 4.2.6 on 2023-11-10 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_password_confirmation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='password1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_confirmation',
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='The entered password is too short.                                              It must contain at least 3 characters.')]),
        ),
    ]
