from django.urls import path, re_path
from .views import EducationView, ExperienceView, AboutView, ServicesView, SkillsView, WorkView, BlogView

urlpatterns = [
    path('education/', EducationView.as_view(), name='education'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('work/', WorkView.as_view(), name='work'),
    path('blog/', BlogView.as_view(), name='blog'),
]