from django import template
from django.template.defaultfilters import stringfilter
from extensions.time_utils import numbers_to_persian

register = template.Library()

@register.filter
@stringfilter
def to_persian(string):
    return numbers_to_persian(string)
