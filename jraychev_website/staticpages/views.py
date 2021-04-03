from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from staticpages.models import Skills, Testimonials, Education, Experience, Project, Service
from accounts.models import CustomUser


class EducationView(TemplateView):
    template_name = 'staticpages/education.html'

    def get_context_data(self, **kwargs):
        context =  super(EducationView,self).get_context_data(**kwargs)

        educations = Education.objects.all()

        context['educations'] = educations

        return context 

class ExperienceView(TemplateView):
    template_name = 'staticpages/experience.html'

    def get_context_data(self, **kwargs):
        context =  super(ExperienceView,self).get_context_data(**kwargs)

        experiences = Experience.objects.all().order_by('-experience_year')

        context['experiences'] = experiences

        return context 

class AboutView(TemplateView):
    template_name = 'staticpages/about.html'

    def get_context_data(self, **kwargs):
        context =  super(AboutView,self).get_context_data(**kwargs)

        skills = Skills.objects.all()
        quotes = Testimonials.objects.all()
        jraychev_about = CustomUser.objects.filter(id=1).values('about')

        context['skills'] = skills
        context['quotes'] = quotes
        context['jraychev_about'] = jraychev_about

        return context  

class ServicesView(TemplateView):
    template_name = 'staticpages/services.html'

    def get_context_data(self, **kwargs):
        context =  super(ServicesView,self).get_context_data(**kwargs)

        services = Service.objects.all()

        context['services'] = services

        return context

class SkillsView(TemplateView):
    template_name = 'staticpages/skills.html'

class ProjectView(TemplateView):
    template_name = 'staticpages/projects.html'

    def get_context_data(self, **kwargs):
        context =  super(ProjectView,self).get_context_data(**kwargs)

        projects = Project.objects.all()

        context['projects'] = projects

        return context

class BlogView(TemplateView):
    template_name = 'staticpages/blog.html'    
    