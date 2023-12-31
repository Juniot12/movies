# Generated by Django 4.2.7 on 2023-12-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='bookingdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mname', models.CharField(max_length=40)),
                ('theatre_name', models.CharField(max_length=30)),
                ('no_oftickets', models.IntegerField()),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('language', models.CharField(max_length=20)),
                ('payment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='moviedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mname', models.CharField(max_length=100)),
                ('date_release', models.DateField()),
                ('rating', models.IntegerField()),
                ('theatre_name', models.CharField(max_length=50)),
                ('seat_available', models.CharField(max_length=3)),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phonennumber', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
