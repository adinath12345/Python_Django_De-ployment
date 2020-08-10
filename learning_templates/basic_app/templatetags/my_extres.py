from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    # It cuts the the all avlues in the argument

    return value.replace(arg,'')

# register.filter('cut',cut)