# Generated by Django 3.0 on 2020-04-17 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drbotapp', '0005_auto_20200417_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(default='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
