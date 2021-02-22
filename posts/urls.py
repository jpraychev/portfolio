from django.urls import path, re_path
from .views import PostsView, \
                    PostsDetailView, \
                    TagView, tag_view, \
                    CategoryView, cat_view, \
                    PostCreateView, create_view, \
                    BeforePostCreateView

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostsView.as_view(), name='all-posts'),
    path('<int:pk>', PostsDetailView.as_view(), name='post-detail'),
    
    # re_path(r'^tags/(?P<tag_name>[A-Za-z_]*)/$', tag_view, name='tag-view'), # FBV with re
    # path('tags/<slug:tag_name>/', tag_view, name='tag-view') # FBV with only slug 
    path('tags/<tag_name>/', TagView.as_view(), name='tag-view-cbv'), # CBV

    # re_path(r'^category/(?P<cat_name>[A-Za-z_]*)/$', cat_view, name='cat-view'), # FBV with re
    # path('category/<slug:cat_name>/', cat_view, name='cat-view') # FBV with only slug 
    path('category/<cat_name>/', CategoryView.as_view(), name='cat-view-cbv'), # CBV

    # path('create/', create_view, name='post-create-fbv'), # CBV
    path('create/', PostCreateView.as_view(), name='post-create-cbv'), # CBV  

    path('create/initial', BeforePostCreateView.as_view(), name='initial-post-create')  
]