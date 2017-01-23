from django import template
from django.template.defaultfilters import stringfilter
from rest_framework.utils.formatting import markup_description


register = template.Library()


@register.filter(name='markdown')
@stringfilter
def markdown(value):
    return markup_description(value)


@register.filter(name='first_arg_split_by_slash')
@stringfilter
def split_by_slash(value, name_parent):
    value = value.split(name_parent)[1]
    result = value.split('/')[1]
    return result if result else name_parent
