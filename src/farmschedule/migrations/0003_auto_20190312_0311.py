# Generated by Django 2.1.7 on 2019-03-12 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmschedule', '0002_auto_20190312_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrydb',
            name='country',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
