# Generated by Django 4.1.4 on 2022-12-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residences', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceinfo',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
