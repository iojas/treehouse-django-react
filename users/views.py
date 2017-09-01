# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
# Create your views here.

def dashboard(req):
  return render(req, 'users/dashboard.html')

class LogoutView(LoginRequiredMixin, FormView):
  form_class = forms.LogoutForm
  template_name = 'users/logout.html'
  def form_valid(self, form):
    logout(self.request)
    return HttpResponseRedirect(reverse('home'))
