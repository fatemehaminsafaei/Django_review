from django import template

register = template.Library()

@register.tag(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter(name='lower')
def lower(value):
    return value.lower()

@register.simple_tag
def numposts(obs, word):
    if len(obs) > 1 or len(obs) == 0:
        word = word + 's'
    return ' '.join([str(len(obs)), word])
