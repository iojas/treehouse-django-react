# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .. import forms
from ..models import *
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import SetHeadlineMixin

# Create your views here.
class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
  form_class = forms.CompanyForm
  headline = 'Create Company'
  success_url = reverse_lazy('users:dashboard')
  template_name = 'groups/company/form.html'

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    response = super(Create, self).form_valid(form)
    self.object.members.add(self.request.user)
    return response

class Update(LoginRequiredMixin, SetHeadlineMixin,  generic.UpdateView):
  form_class = forms.CompanyForm
  template_name = 'groups/company/form.html'
  success_url = reverse_lazy('users:dashboard')

  def get_queryset(self):
  	return self.request.user.companies.all()

  def get_headline(self):
  	return 'Edit' + ' ' + self.object.name

class Detail(LoginRequiredMixin, SetHeadlineMixin,  generic.FormView):
  template_name = 'groups/company/detail.html'
  headline = 'detail'
  form_class = forms.CompanyInviteForm

  def get_success_url(self):
    self.get_object()
    return reverse('groups:companies:detail', kwargs={
        'slug': self.object.slug})

  def  get_object(self):
    self.object = self.request.user.companies.get(
        slug = self.kwargs.get('slug')
      )
    return self.object

  def get_queryset(self):
  	return self.request.user.companies.all()

  def get_context_data(self, **kwargs):
    context = super(Detail, self).get_context_data(**kwargs)
    context['object'] = self.get_object()
    return context

  def form_valid(self, form):
    response = super(Detail, self).form_valid(form)
    CompanyInvite.objects.create(
        from_user = self.request.user,
        to_user = form.invitee,
        company = self.get_object()
      )
    return response
