from django.contrib import admin
from .models import Skills

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name' , 'skill_percent' , 'skill_class')
