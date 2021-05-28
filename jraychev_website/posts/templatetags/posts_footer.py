from django import template
from posts.models import Category, Tag
from accounts.models import UserSocial

register = template.Library()

@register.inclusion_tag('posts/footer.html', takes_context=True)
def get_footer(context):
    request = context['request']
    tags = Tag.objects.all()[:5]
    categories = Category.objects.all()[:5]
    user_social = UserSocial.objects.filter(user=1)
    return {
        'tags' : tags, 
        'categories' : categories,
        'user_social' : user_social,
        'request': request
    }