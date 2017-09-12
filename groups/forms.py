from django import forms
from .models import *

class CompanyForm(forms.ModelForm):
	class Meta:
		fields = ('name', 'description')
		model = Company
	
class FamilyForm(forms.ModelForm):
	class Meta:
		fields = ('name', 'description')
		model = Family