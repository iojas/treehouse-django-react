# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 20:26
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20170910_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='family',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
