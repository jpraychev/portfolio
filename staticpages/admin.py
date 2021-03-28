from django.contrib import admin
from .models import Skills, Testimonials, Education

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name' , 'skill_percent' , 'skill_class')

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('quote_text' , 'quote_author' , 'quote_author_company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name' , 'degree_field' , 'degree_year', 'degree_description')