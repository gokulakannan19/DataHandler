# Generated by Django 4.1 on 2022-08-10 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accound_name',
            new_name='account_name',
        ),
    ]
