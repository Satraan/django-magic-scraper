# Generated by Django 2.2.6 on 2019-10-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicscraper', '0008_card_collectornumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='tcgPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
    ]