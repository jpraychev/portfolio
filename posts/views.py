from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from django.urls import reverse_lazy, reverse
from .models import Tag, Category, Post

# Create your views here.

class PostsView(ListView):

    # paginate_by = 10
    model = Post
    context_object_name = 'all_posts'
    template_name = 'posts/all_posts.html'
    # login_url = reverse_lazy('login')


class PostsDetailView(DetailView):

    model = Post
    template_name = 'posts/post_detail.html'

def tag_view(request, tag_name):
    

    # try:
    tag = Tag.objects.filter(name=tag_name).values_list('id', flat=True)

    if not tag:
        print('Query set is empty. Reeturn message to user')
        return 
    else:
        for x in tag:
            tag_id = x
        posts_by_tag = Post.objects.filter(tags=tag_id)
        return render(request, 'posts/posts_tag.html', {'posts_by_tag': posts_by_tag})
        
    # except Exception as error:
    #     print(error)
    #     return render(request, 'home/index.html')

    