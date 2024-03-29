from django.contrib import admin
from .models import Skills, Testimonials, Education, Experience, Project, Service, Menu


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name' , 'skill_percent' , 'skill_class', 'skill_color')


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('quote_text' , 'quote_author' , 'quote_author_company', 'quote_color')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name' , 'degree_field' , 'degree_year', 'degree_description')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('experience_name' , 'experience_field' , 'experience_year', 'experience_description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name' , 'project_homepage', 'project_description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name' , 'service_description', 'service_icon', 'service_color')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_slug')