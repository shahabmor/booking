# Generated by Django 4.1.4 on 2022-12-31 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_airplaneticketfacility_delete_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirPlaneTicketPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('airplane_ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='tickets.airplaneticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
    ]
