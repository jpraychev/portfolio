from django.shortcuts import render
from django.http import JsonResponse
from posts.models import Post, Category # Import models
from subscribe.models import Subscribe
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

def posts(request):
    ''' API view that returns title and category name of all posts
    '''
    posts = Post.objects.values('id', 'title', 'category__name')
    data = {
        'posts' : list(posts)
    }
    return JsonResponse(data)


# API view for subscribers list
def subscribers(request):
    print(request)
    ''' API view that return list of all subscribers. Users should be authenticated prior GET request
    '''
    subscribers = Subscribe.objects.values('email', 'date_submitted')
    data = {
        'subscribers' : list(subscribers)
    }
    return JsonResponse(data)


@csrf_exempt
def subscribe(request):
    '''API view that saves user provided email as subscriber to the database
    '''
    if request.POST:
        if 'email' not in request.POST:
            return HttpResponse('Bad POST Parameters. Please use "email" key')
        user_email = request.POST['email']
        subscribers_list = Subscribe.objects.values_list('email', flat=True)
        if user_email not in subscribers_list:
            subscribe = Subscribe(email=user_email)
            subscribe.save()
            return HttpResponse('You have successfully subscribed!')
        return HttpResponse('User already exists')      
    else:
        raise PermissionDenied