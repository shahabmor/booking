# Generated by Django 4.1.4 on 2022-12-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_priceinfo_policy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airplaneticket',
            name='date',
        ),
        migrations.AlterField(
            model_name='airplaneticket',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
