# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_remove_feedback_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
