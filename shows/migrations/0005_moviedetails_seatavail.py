# Generated by Django 5.0 on 2023-12-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_alter_bookingdetails_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='seatAvail',
            field=models.IntegerField(default=150),
            preserve_default=False,
        ),
    ]
