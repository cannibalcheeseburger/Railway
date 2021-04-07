# Generated by Django 3.1.7 on 2021-04-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('train_id', models.IntegerField()),
                ('num_booked', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('train_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('seats_total', models.IntegerField()),
                ('seats_res', models.IntegerField()),
                ('_type', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
    ]