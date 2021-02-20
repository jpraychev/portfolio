from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Tag, Category, Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

# Define private variables for views
_PAGINATE_BY = 5

class PostsView(ListView):

    paginate_by = _PAGINATE_BY
    # model = Post
    queryset = Post.objects.filter(status=0) # Return only post with status publish
    context_object_name = 'all_posts'
    template_name = 'posts/all_posts.html'
    login_url = reverse_lazy('login')

class PostsDetailView(DetailView):

    # model = Post
    queryset = Post.objects.filter(status=0)
    template_name = 'posts/post_detail.html'

# FBV - passing url parameters
def tag_view(request, tag_name):

    searched_tag = Tag.objects.filter(name=tag_name).values_list('id', flat=True)

    tag_id = get_object_or_404(searched_tag)
    posts_by_tag = Post.objects.filter(tags=tag_id, status=0)

    paginator = Paginator(posts_by_tag, _PAGINATE_BY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/posts_tag.html', {'posts_by_tag': posts_by_tag, 'page_obj': page_obj,})

# CBV - passing url parameters
class TagView(ListView):

    template_name = 'posts/posts_tag.html'
    context_object_name = 'posts_by_tag'
    paginate_by = _PAGINATE_BY

    def get_queryset(self):
        # Get tag_name from URL
        # self.kwargs['tag_name'] holds the parameter from URL - urls.py <tag_name>
        searched_tag = Tag.objects.filter(name=self.kwargs['tag_name']).values_list('id', flat=True)

        # Get object or throw 404
        tag_id = get_object_or_404(searched_tag)

        return Post.objects.filter(tags=tag_id, status=0)


# FBV - passing url parameters
def cat_view(request, cat_name):

    category = Category.objects.filter(name=cat_name)

    cat_id = get_object_or_404(category)
    posts_by_cat = Post.objects.filter(category=cat_id, status=0)

    paginator = Paginator(posts_by_cat, _PAGINATE_BY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/posts_cat.html', {'posts_by_cat' : posts_by_cat, 'page_obj': page_obj})

# CBV - passing url parameters
class CategoryView(ListView):
    
    template_name = 'posts/posts_cat.html'
    context_object_name = 'posts_by_cat'
    paginate_by = _PAGINATE_BY

    def get_queryset(self):
        # Get cat_name from URL
        # self.kwargs['cat_name'] holds the parameter from URL - urls.py <cat_name>
        searched_cat = Category.objects.filter(name=self.kwargs['cat_name']).values_list('id', flat=True)
        print(searched_cat)
        # Get object or throw 404
        cat_id = get_object_or_404(searched_cat)

        return Post.objects.filter(category=cat_id, status=0)



def create_view(request):
    pass

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'content', 'tags', 'category']
    success_url = reverse_lazy('all-posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 2 # Status set to Preview, instead of Publish
        return super().form_valid(form)
