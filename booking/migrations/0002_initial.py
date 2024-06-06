# Generated by Django 5.0.6 on 2024-05-30 18:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('flight', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.passenger'),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.seat'),
        ),
        migrations.AddField(
            model_name='baggage',
            name='booking_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.bookingdetail'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='booking_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.bookingdetail'),
        ),
    ]
