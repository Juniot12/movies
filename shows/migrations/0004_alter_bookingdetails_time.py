# Generated by Django 5.0 on 2023-12-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_remove_bookingdetails_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='time',
            field=models.CharField(max_length=40),
        ),
    ]
