# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='company',
            name='members',
        ),
        migrations.RemoveField(
            model_name='family',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='family',
            name='members',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
    ]
