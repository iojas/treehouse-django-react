from django import template

register = template.Library()

from ..forms import ThoughtForm

@register.inclusion_tag('thoughts/_forms.html')

def thought_form():
	form = ThoughtForm()
	return {'form' : form}