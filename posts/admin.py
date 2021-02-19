from django.contrib import admin
from .models import Tag, Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title', 'author', 'date_posted', 'status')
    save_as = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')



