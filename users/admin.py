# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Family)

admin.site.register(models.Company)
