# Generated by Django 5.0.6 on 2024-06-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_flight_terminal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='terminal',
        ),
        migrations.AddField(
            model_name='flight',
            name='destination_terminal',
            field=models.CharField(default='Terminal 2', max_length=50),
        ),
        migrations.AddField(
            model_name='flight',
            name='origin_terminal',
            field=models.CharField(default='Terminal 1', max_length=50),
        ),
    ]