# Generated by Django 3.0 on 2020-04-26 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drbotapp', '0004_auto_20200425_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rparobotconfig',
            name='botjson',
        ),
    ]
