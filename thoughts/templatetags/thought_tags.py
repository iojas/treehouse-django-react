import json
import datetime
from django import template
from django.utils import timezone
register = template.Library()

from ..forms import ThoughtForm
from ..models import Thoughts

@register.inclusion_tag('thoughts/_forms.html')

def thought_form():
	form = ThoughtForm()
	return {'form' : form}

@register.simple_tag(takes_context = True)
def chart_data(context):
	user = context['user']
	ten_days_ago = timezone.now() - datetime.timedelta(days=10)
	thoughts = user.thoughts.filter(recorded_at__gte=ten_days_ago)
	return json.dumps ({
		'labels': [thought.recorded_at.strftime('%Y-%m-%d') for 
					thought in thoughts],
		'series': [[thought.condition for thought in thoughts]]
	})
	