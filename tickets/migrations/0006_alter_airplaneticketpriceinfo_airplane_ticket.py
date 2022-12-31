# Generated by Django 4.1.4 on 2022-12-31 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_airplaneticketpriceinfo_delete_priceinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplaneticketpriceinfo',
            name='airplane_ticket',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_info', to='tickets.airplaneticket'),
        ),
    ]