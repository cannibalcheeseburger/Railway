# Generated by Django 3.1.7 on 2021-04-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0009_auto_20210405_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='password',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='uid',
            new_name='username',
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='password2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
