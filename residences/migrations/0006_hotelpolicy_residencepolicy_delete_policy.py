# Generated by Django 4.1.4 on 2022-12-28 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residences', '0005_hotelfacility_residencefacility_unitfacility_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='residences.hotel')),
            ],
            options={
                'verbose_name_plural': 'hotel_policies',
            },
        ),
        migrations.CreateModel(
            name='ResidencePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('residence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='residences.residence')),
            ],
            options={
                'verbose_name_plural': 'residence_policies',
            },
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
    ]
