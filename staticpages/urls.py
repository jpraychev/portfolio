from django.urls import path, re_path
from .views import EducationView

urlpatterns = [
    path('education/', EducationView.as_view(), name='education'),
]