# Generated by Django 3.2.3 on 2021-05-26 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20210202_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 18, 52, 12, 994425)),
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]