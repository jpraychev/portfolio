from django.urls import path, re_path
from .views import ContactView

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]