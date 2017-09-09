# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ThoughtForm
# Create your views here.

class CreateThoughts(LoginRequiredMixin, CreateView):
	form_class = ThoughtForm 
	success_url = reverse_lazy('users:dashboard')
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateThoughts, self).form_valid(form)
