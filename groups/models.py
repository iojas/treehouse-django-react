# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from uuid import uuid4
import uuid
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.dispatch import receiver 
# Create your models here.

class Group(models.Model):
	created_at = models.DateTimeField(default = timezone.now)
	created_by = models.ForeignKey(User, related_name = '%(class)s_created')
	name = models.CharField(max_length=255)
	slug = AutoSlugField(populate_from = 'name')
	description = models.TextField(default='')

	class Meta:
		abstract = True

	def __str__(self)	:
		return self.name

class Family(Group):
	members = models.ManyToManyField(User, related_name='families')

	class Meta:
		verbose_name_plural = 'families'

class Company(Group):
	members = models.ManyToManyField(User, related_name='companies')

	class Meta:
		verbose_name_plural = 'companies'

INVITE_STATUSES =(
		(0,'Pending'),
		(1,'Accepted'),
		(2,'Rejected')
	)

class Invite(models.Model):
	from_user = models.ForeignKey(User, related_name='%(class)s_created')
	to_user = models.ForeignKey(User, related_name='%(class)s_received')
	status = models.IntegerField(default=0, choices = INVITE_STATUSES)
	uuid = models.CharField(max_length=32, default='')

	class Meta:
		abstract = True

	def __str__(self):
		return str(self.to_user) + " invited by "+ str(self.from_user)

	def save(self, *args, **kwargs):
		if not self.pk:
			self.uuid = uuid.uuid4().hex
		super(Invite, self)	.save(*args, **kwargs)

class CompanyInvite(Invite):
	company = models.ForeignKey(Company, related_name='invites')

	def __str__(self):
		return str(super(CompanyInvite, self).__str__()) + " to " + str(self.company)

class FamilyInvite(Invite):
	family = models.ForeignKey(Family, related_name='invites')
