# Generated by Django 4.2.6 on 2023-11-06 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_surname_user_last_name_remove_user_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='id_password',
        ),
    ]