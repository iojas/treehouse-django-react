# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.views import generic
from braces.views import SelectRelatedMixin
from django.contrib.auth.models import User

# Create your views here.

class dashboard(LoginRequiredMixin, SelectRelatedMixin, generic.TemplateView):
	model = User
  	template_name = 'users/dashboard.html'
  	select_related = ('thoughts',)
  	
  	def get_objects(self, queryset=None):
  		return self.request.user


class LogoutView(LoginRequiredMixin, FormView):
  form_class = forms.LogoutForm
  template_name = 'users/logout.html'
  def form_valid(self, form):
    logout(self.request)
    return HttpResponseRedirect(reverse('home'))

class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'users/signup.html'
  success_url = reverse_lazy('users:dashboard')
