# Generated by Django 3.1.7 on 2021-04-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_auto_20210428_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='date',
            field=models.DateField(),
        ),
    ]