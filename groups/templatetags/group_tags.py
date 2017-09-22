from django import template

register = template.Library()

@register.inclusion_tag('groups/_badge.html', takes_context = True)
def invite_badge(context, invite_type):
	if invite_type == 'family':
		return {'invite_count': context['user'].familyinvite_received.filter(status = 0).count()}
	else:
		return {'invite_count': context['user'].companyinvite_received.filter(status = 0).count()}