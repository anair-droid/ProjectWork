# Generated by Django 3.0 on 2020-04-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drbotapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tblconfig',
            name='application',
            field=models.CharField(max_length=40),
        ),
    ]