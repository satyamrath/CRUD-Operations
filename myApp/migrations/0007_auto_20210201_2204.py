# Generated by Django 3.1.5 on 2021-02-01 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='document',
            name='creation_time',
        ),
    ]
