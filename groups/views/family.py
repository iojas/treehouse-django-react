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
from django.shortcuts import get_object_or_404


from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Detail(LoginRequiredMixin, SetHeadlineMixin,  generic.FormView):
  template_name = 'groups/family/detail.html'
  headline = 'detail'
  form_class = forms.FamilyInviteForm

  def get_queryset(self):
  	return self.request.user.families.all()

  def get_success_url(self):
    self.get_object()
    return reverse('groups:families:detail', kwargs={
        'slug': self.object.slug})

  def get_object(self):
    self.object = self.request.user.families.get(
        slug = self.kwargs.get('slug')
      )
    return self.object

  def get_context_data(self, **kwargs):
    context = super(Detail, self).get_context_data(**kwargs)
    context['object'] = self.get_object()
    return context

  def form_valid(self, form):
    response = super(Detail, self).form_valid(form)
    FamilyInvite.objects.create(
        from_user = self.request.user,
        to_user = form.invitee,
        family = self.get_object()
      )
    return response

class Invites (LoginRequiredMixin, generic.ListView):
  model = FamilyInvite
  template_name = 'groups/family/invites.html'
  def get_queryset(self):
    return self.request.user.familyinvite_received.filter(status = 0)

class InviteResponse(LoginRequiredMixin, generic.RedirectView):
  url = reverse_lazy('groups:families:invites')

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


class Leave(LoginRequiredMixin, SetHeadlineMixin, generic.FormView):
  form_class = forms.LeaveForm
  template_name = 'groups/family/form.html'
  success_url = reverse_lazy('users:dashboard')

  def get_object(self):
    try:
      self.object = self.request.user.families.filter(
          slug = self.kwargs.get('slug'),
        ).exclude(created_by =  self.request.user).get()
    except models.Family.DoesNotExist:
      raise Http404()

  def get_headline(self):
    return "leave "

  def form_valid(self, form):
    self.get_object()
    self.object.members.remove(self.request.user)
    return super(Leave, self).form_valid(form)

@receiver(post_save, sender = FamilyInvite)
def join_family(sender, instance, created, **kwargs):
  if not created:
    if instance.status == 1:
      instance.family.members.add(instance.to_user)
