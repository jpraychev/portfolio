from django.urls import path, re_path
from .views import posts, subscribers, subscribe
# from .views import PostsView

urlpatterns = [
    path('v1/posts', posts, name='api-posts'),
    path('v1/subscribers', subscribers, name='subscribers'),
    path('v1/subscribe/', subscribe, name='subscribe')
    # re_path(r'^v1/subscribe/(?P<user_email>[A-Za-z_0-9@.]*)/$', subscribe, name='subscribe'),
]