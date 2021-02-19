from django.urls import path, re_path
from .views import PostsView, PostsDetailView, tag_view
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostsView.as_view(), name='all-posts'),
    path('<int:pk>', PostsDetailView.as_view(), name='post-detail'),
    # Both lines are correct!
    re_path(r'^tags/(?P<tag_name>[A-Za-z_]*)/$', tag_view, name='tag-view'),
    # path('tags/<slug:tag_name>/', tag_view, name='tag-view')

    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    # path('<slug>/update', ProfileUpdateView.as_view(), name='profile-update'),
]