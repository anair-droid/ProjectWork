# Generated by Django 3.0 on 2020-04-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drbotapp', '0002_tbltrans'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblJobsch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botname', models.CharField(max_length=100)),
                ('BotJobsch', models.CharField(max_length=100)),
                ('BotProcess', models.CharField(max_length=100)),
            ],
        ),
    ]