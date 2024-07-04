# Generated by Django 5.0.6 on 2024-06-26 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vechile',
            name='number_plate',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='VechileDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('joined_date', models.CharField(max_length=200)),
                ('using_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vechile_driver', to='homepage.vechile')),
            ],
        ),
        migrations.DeleteModel(
            name='GPSDriver',
        ),
    ]
