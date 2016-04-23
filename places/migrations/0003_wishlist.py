# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_profile_pic'),
        ('places', '0002_auto_20160423_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
                ('place', models.ManyToManyField(to='places.Place')),
            ],
        ),
    ]