# Generated by Django 4.1 on 2022-08-11 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_accound_name_account_account_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
            ],
        ),
    ]
