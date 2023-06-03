import os
from django import template


register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)


@register.filter
def make_upper(value):
    return value.title()
