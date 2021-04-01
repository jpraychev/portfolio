from django import template
from staticpages.models import Menu

register = template.Library()

@register.inclusion_tag('home/menu.html', takes_context=True)
def get_menu(context):
    request = context['request']
    menu = Menu.objects.all()
    return {'menu' : menu, 'request': request}