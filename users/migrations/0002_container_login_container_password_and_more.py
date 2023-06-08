# Generated by Django 4.2.1 on 2023-06-08 09:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='login',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='expdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 9, 20, 39, 183244)),
        ),
        migrations.AlterField(
            model_name='container',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='status',
            field=models.CharField(choices=[('e', 'Enabled'), ('d', 'Disabled')], default='e', max_length=1),
        ),
        migrations.AlterField(
            model_name='container',
            name='userid',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]