# Generated by Django 2.2.5 on 2019-09-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicscraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='description',
        ),
        migrations.AddField(
            model_name='merchant',
            name='website',
            field=models.CharField(default='Website', max_length=200),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]