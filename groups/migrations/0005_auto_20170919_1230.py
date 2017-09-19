# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_companyinvite_familyinvite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinvite',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='familyinvite',
            name='accepted',
        ),
        migrations.AddField(
            model_name='companyinvite',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='familyinvite',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
