from django import forms
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q

class CompanyForm(forms.ModelForm):
	class Meta:
		fields = ('name', 'description')
		model = Company

class FamilyForm(forms.ModelForm):
	class Meta:
		fields = ('name', 'description')
		model = Family

class CompanyInviteForm(forms.Form):
  email_or_username = forms.CharField(label = 'Email or Username')

  def clean_email_or_username(self):
    data = self.cleaned_data['email_or_username']
    try:
        self.invitee = User.objects.get(
          Q(email=data)|Q(username=data)
      )
    except User.DoesNotExist:
      raise ValidationError('No Such User')
    return data

class FamilyInviteForm(forms.Form):
  email_or_username = forms.CharField(label = 'Email or Username')

  def clean_email_or_username(self):
    data = self.cleaned_data['email_or_username']
    try:
        self.invitee = User.objects.get(
          Q(email=data)|Q(username=data)
      )
    except User.DoesNotExist:
      raise ValidationError('No Such User')
    return data

class LeaveForm(forms.Form):
  pass
