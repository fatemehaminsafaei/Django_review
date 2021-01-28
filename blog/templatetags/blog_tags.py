from django import template

register = template.Library()

@register.tag(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter(name='lower')
def lower(value):
    return value.lower()


