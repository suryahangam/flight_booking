# Generated by Django 5.0.6 on 2024-06-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0009_remove_flight_terminal_flight_destination_terminal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_aisle_seat',
            field=models.BooleanField(default=False),
        ),
    ]
