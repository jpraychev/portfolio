from django.urls import path, re_path
from .views import posts
# from .views import PostsView

urlpatterns = [
    path('v1/posts', posts, name='api-posts'),
]