# Generated by Django 5.0.6 on 2024-05-31 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='basic_rate',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
