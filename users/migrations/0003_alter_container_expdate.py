# Generated by Django 4.2.1 on 2023-06-08 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_container_login_container_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='expdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 9, 22, 51, 875632)),
        ),
    ]