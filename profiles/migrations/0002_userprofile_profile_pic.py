# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.URLField(null=True),
        ),
    ]
