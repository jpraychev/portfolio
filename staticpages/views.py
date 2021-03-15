from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin


class EducationView(TemplateView):
    template_name = 'staticpages/education.html'

class ExperienceView(TemplateView):
    template_name = 'staticpages/experience.html'

class AboutView(TemplateView):
    template_name = 'staticpages/about.html'