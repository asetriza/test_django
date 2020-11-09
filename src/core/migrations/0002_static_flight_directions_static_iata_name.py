# Generated by Django 3.0.5 on 2020-11-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Static_flight_directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fly_from', models.CharField(max_length=10)),
                ('fly_to', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Static_iata_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_name', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=150)),
            ],
        ),
    ]