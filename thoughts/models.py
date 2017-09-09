# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
CONDITIONS = (
  (1, 'Joy'),
  (5, 'Passionate'),
  (10, 'Happy'),
  (20, 'Positive'),
  (25, 'Optimistic'),
  (30, 'Content'),
  (35, 'Boared'),
  (40, 'Pessimistic'),
  (45, 'Angry'),
  (50, 'Jelouse'),
)

class Thoughts(models.Model):
  user = models.ForeignKey(User, related_name = 'thoughts')
  recorded_at = models.DateTimeField(default = timezone.now, editable = False)
  condition = models.IntegerField(choices = CONDITIONS)
  notes = models.TextField(blank= True, default='')

  def __unicode__(self):
    return '{}:{}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.get_condition_display())

  class Meta:
    ordering = ['-recorded_at']  