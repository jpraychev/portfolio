from posts.models import Tag, Category
from accounts.models import UserSocial

def render_footer(request):
    ''' Returns necessary information for footer rendering
    '''
    tags = Tag.objects.all()[:5]
    categories = Category.objects.all()[:5]
    user_socials = UserSocial.objects.filter(user=1) # 1 is ID of user. In this case jraychev. Maybe a future rework?

    return {
        'tags' : tags,
        'categories' : categories,
        'user_socials' : user_socials,
    }