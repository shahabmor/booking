# Generated by Django 4.1.4 on 2022-12-24 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residences', '0003_alter_priceinfo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renthotel',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2022, 12, 24)),
        ),
        migrations.AlterField(
            model_name='rentresidence',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2022, 12, 24)),
        ),
    ]