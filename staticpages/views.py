from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from staticpages.models import Skills, Testimonials


class EducationView(TemplateView):
    template_name = 'staticpages/education.html'

class ExperienceView(TemplateView):
    template_name = 'staticpages/experience.html'

class AboutView(TemplateView):
    template_name = 'staticpages/about.html'

    def get_context_data(self, **kwargs):
        context =  super(AboutView,self).get_context_data(**kwargs)

        skills = Skills.objects.all()
        quotes = Testimonials.objects.all()

        context['skills'] = skills
        context['quotes'] = quotes

        return context  

class ServicesView(TemplateView):
    template_name = 'staticpages/services.html'

class SkillsView(TemplateView):
    template_name = 'staticpages/skills.html'

class WorkView(TemplateView):
    template_name = 'staticpages/work.html'

class BlogView(TemplateView):
    template_name = 'staticpages/blog.html'    
    