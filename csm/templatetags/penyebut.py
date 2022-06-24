from django import template

register = template.Library()

@register.simple_tag
def level(value):
    """memberikan string penyebut dari setiap value csm"""
    if(value >= 0 and value < 1):
        return 'Level 0'
    if(value >= 1 and value < 1.5):
        return 'Level 1'
    if(value >= 1.5 and value < 2.5):
        return 'Level 2'
    if(value >= 2.5 and value < 3.5):
        return 'Level 3'
    if(value >= 3.5 and value < 4.5):
        return 'Level 4'
    if(value >= 4.5):
        return 'Level 5'
    # return value.replace(arg, '')