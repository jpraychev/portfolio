from django import template
from staticpages.models import Menu
from accounts.models import UserSocial, CustomUser
from django.shortcuts import get_object_or_404

register = template.Library()

@register.inclusion_tag('home/menu.html', takes_context=True)
def get_menu(context):
    request = context['request']
    menu = Menu.objects.all()
    return {'menu' : menu, 'request': request}

@register.inclusion_tag('home/user_social.html')
def get_social(user):
    user_social = UserSocial.objects.filter(user=user)
    return { 'user_social' : user_social }

@register.inclusion_tag('home/user_meta.html', takes_context=True)
def get_user_meta(context, id):
    request = context['request']
    user_data = get_object_or_404(CustomUser.objects.filter(id=id).values('username', 'first_name', 'last_name', 'profession', 'profile_image'))
    return { 'user_data' : user_data, 'request': request }