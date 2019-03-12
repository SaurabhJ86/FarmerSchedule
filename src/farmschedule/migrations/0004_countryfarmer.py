# Generated by Django 2.1.7 on 2019-03-12 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmschedule', '0003_auto_20190312_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryFarmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('language', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmschedule.CountryDB')),
            ],
        ),
    ]