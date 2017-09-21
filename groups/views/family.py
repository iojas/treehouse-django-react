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
  form_class = forms.FamilyForm
  headline = 'Create Family'
  success_url = reverse_lazy('users:dashboard')
  template_name = 'groups/family/form.html'

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    response = super(Create, self).form_valid(form)
    self.object.members.add(self.request.user)
    return response

class Update(LoginRequiredMixin, SetHeadlineMixin,  generic.UpdateView):
  form_class = forms.FamilyForm
  template_name = 'groups/family/form.html'
  success_url = reverse_lazy('users:dashboard')

  def get_queryset(self):
  	return self.request.user.families.all()

  def get_headline(self):
  	return 'Edit' + ' ' + self.object.name

class Detail(LoginRequiredMixin, SetHeadlineMixin,  generic.DetailView):
  template_name = 'groups/family/detail.html'
  headline = 'detail'
  def get_queryset(self):
  	return self.request.user.families.all()

class Invites (LoginRequiredMixin, generic.ListView):
  model = FamilyInvite
  template_name = 'groups/family/invites.html'
  def get_queryset(self):
    return self.request.user.companyinvite_received.filter(status = 0)

class InviteResponse(LoginRequiredMixin, generic.RedirectView):
  url = reverse_lazy('groups:family:invites')

  def get(self, request, *args, **kwargs):
    invite = get_object_or_404(
        FamilyInvite,
        to_user = request.user,
        uuid = kwargs.get('code'),
        status = 0
      )
    if kwargs.get('response') == 'accept':
      invite.status = 1
    else:
      invite.status = 2

    invite.save()
    return super(InviteResponse, self).get(request, *args, **kwargs)

@receiver(post_save, sender = FamilyInvite)
def join_family(sender, instance, created, **kwargs):
  if not created:
    if instance.status == 1:
      instance.family.members.add(instance.to_user)
