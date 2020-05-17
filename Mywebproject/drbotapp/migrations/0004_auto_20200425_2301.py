# Generated by Django 3.0 on 2020-04-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drbotapp', '0003_appconfig_applob'),
    ]

    operations = [
        migrations.CreateModel(
            name='appinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=100)),
                ('appdesc', models.CharField(max_length=100)),
                ('applob', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='botmachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machinename', models.CharField(max_length=100)),
                ('machineIP', models.CharField(max_length=100)),
                ('machinedesc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='rparobotconfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botname', models.CharField(max_length=100)),
                ('botdesc', models.CharField(max_length=100)),
                ('botServerID', models.URLField(blank=True)),
                ('botjson', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='rpaserverConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applob', models.CharField(max_length=100)),
                ('appname', models.CharField(max_length=100)),
                ('appUrl', models.URLField(blank=True)),
                ('appAPIkey', models.CharField(max_length=100)),
                ('param', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='appConfig',
        ),
    ]
