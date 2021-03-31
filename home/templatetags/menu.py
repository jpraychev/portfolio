from django import template
from staticpages.models import Menu

register = template.Library()

@register.inclusion_tag('home/menu.html')
def get_menu():
    menu = Menu.objects.all()
    return {'menu' : menu}