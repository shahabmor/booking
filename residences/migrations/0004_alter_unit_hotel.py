# Generated by Django 4.1.4 on 2022-12-20 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residences', '0003_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='residences.hotel'),
        ),
    ]
