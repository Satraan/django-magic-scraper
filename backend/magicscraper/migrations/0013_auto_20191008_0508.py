# Generated by Django 2.2.6 on 2019-10-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicscraper', '0012_remove_card_setname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='tcgPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]
