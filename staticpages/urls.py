from django.urls import path, re_path
from .views import EducationView, ExperienceView

urlpatterns = [
    path('education/', EducationView.as_view(), name='education'),
    path('experience/', ExperienceView.as_view(), name='experience'),
]