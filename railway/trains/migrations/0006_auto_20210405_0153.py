# Generated by Django 3.1.7 on 2021-04-04 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0005_auto_20210405_0111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Trains',
            new_name='trains',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Users',
            new_name='users',
        ),
    ]
