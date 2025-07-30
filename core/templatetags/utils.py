from django import template

register = template.Library()

@register.filter
def resolve(obj, attr):
    try:
        return obj[attr] # jik dictionary
    except:
        return getattr(obj, attr, '') # jika object