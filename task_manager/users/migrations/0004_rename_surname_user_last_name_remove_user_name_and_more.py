# Generated by Django 4.2.6 on 2023-11-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_full_name_user_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]