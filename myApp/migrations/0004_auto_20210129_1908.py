# Generated by Django 3.1.5 on 2021-01-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20210129_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(default='', upload_to='media/myApp/document_files'),
        ),
    ]