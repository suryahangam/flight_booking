# Generated by Django 5.0.6 on 2024-06-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_alter_flight_flight_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
