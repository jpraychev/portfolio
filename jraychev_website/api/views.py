from django.shortcuts import render
from django.http import JsonResponse
from posts.models import Post, Category # Import models

def posts(request):
    ''' API view that returns title and category name of all posts
    '''
    posts = Post.objects.values('title', 'category__name')
    data = {
        'posts' : list(posts)
    }
    return JsonResponse(data)

        