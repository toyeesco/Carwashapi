# Generated by Django 4.1.2 on 2022-10-11 21:35

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarWash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=250)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('vehicle', models.CharField(choices=[('CAR', 'CAR'), ('BICYCLE', 'BICYCLE'), ('TRUCK', 'TRUCK'), ('CASTER', 'CASTER')], max_length=200)),
                ('services', models.CharField(choices=[('VACUUM', 'VACUUM'), ('WAX', 'WAX'), ('TIREBLACK', 'TIREBLACK'), ('WASH', 'WASH')], max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=200)),
                ('date', models.DateField()),
                ('car_wash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.carwash')),
            ],
        ),
    ]