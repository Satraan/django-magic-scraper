# Generated by Django 2.2.6 on 2019-10-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magicscraper', '0004_auto_20191007_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='editionCode',
            new_name='setCode',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='editionName',
            new_name='setName',
        ),
    ]
