from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, CreateView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Tag, Category, Post
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreateForm, PostUpdateForm
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from accounts.models import UserSocial

# Define private variables for views
_PAGINATE_BY = 5

class PostsView(LoginRequiredMixin, ListView):

    paginate_by = _PAGINATE_BY
    # model = Post
    queryset = Post.objects.filter(status=0) # Return only post with status publish
    context_object_name = 'all_posts'
    template_name = 'posts/all_posts.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get object for a filtered queryset for featured posts
        # Always return the a single featured post, maybe filter by date (new first)
        featured_post = Post.objects.filter(featured=True).order_by('-date_posted')[:1]
        categories = Category.objects.all()[:5]
        tags = Tag.objects.all()[:5]
        
        context['featured_post'] = featured_post
        context['categories'] = categories
        context['tags'] = tags
        return context

class PostsDetailView(LoginRequiredMixin, DetailView):

    # model = Post
    queryset = Post.objects.filter(status=0)
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs: dict) -> 'dict':
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['pk']
        # Get post category id from post_id
        post_cat_id = get_object_or_404(Post.objects.filter(id=post_id).values_list('category', flat=True))
        # Get related posts from post's category and limit the queryset by 3
        related_posts = Post.objects.filter(category=post_cat_id)[:3]
        print(related_posts)
        context['related_posts'] = related_posts
        return context

# FBV - passing url parameters
# def tag_view(request, tag_name):

#     searched_tag = Tag.objects.filter(name=tag_name).values_list('id', flat=True)

#     tag_id = get_object_or_404(searched_tag)
#     posts_by_tag = Post.objects.filter(tags=tag_id, status=0)

#     paginator = Paginator(posts_by_tag, _PAGINATE_BY)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'posts/posts_tag.html', {'posts_by_tag': posts_by_tag, 'page_obj': page_obj,})

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searched_tag = self.kwargs['tag_name']
        context['searched_tag'] = searched_tag
        return context

# FBV - passing url parameters
# def cat_view(request, cat_name):

#     category = Category.objects.filter(name=cat_name)

#     cat_id = get_object_or_404(category)
#     posts_by_cat = Post.objects.filter(category=cat_id, status=0)

#     paginator = Paginator(posts_by_cat, _PAGINATE_BY)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'posts/posts_cat.html', {'posts_by_cat' : posts_by_cat, 'page_obj': page_obj})

# CBV - passing url parameters
class CategoryView(ListView):
    
    template_name = 'posts/posts_cat.html'
    context_object_name = 'posts_by_cat'
    paginate_by = _PAGINATE_BY

    def get_queryset(self):
        # Get cat_name from URL
        # self.kwargs['cat_name'] holds the parameter from URL - urls.py <cat_name>
        # print(self.kwargs['cat_name'])
        # print(Category.objects.filter(name='Linux'))
        searched_cat = Category.objects.filter(name=self.kwargs['cat_name']).values_list('id', flat=True)
        print(searched_cat)
        # Get object or throw 404
        cat_id = get_object_or_404(searched_cat)

        return Post.objects.filter(category=cat_id, status=0)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            searched_category = self.kwargs['cat_name']
            context['searched_category'] = searched_category
            return context
# def create_view(request):
#     pass

class BeforePostCreateView(LoginRequiredMixin, FormView):

    template_name = 'posts/before_post_create.html'
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            request.session['title'] = form.cleaned_data.get('title')
            request.session['content'] = form.cleaned_data.get('content')
            return HttpResponseRedirect(reverse('post-create-cbv'))
        else:
            print('False')
        
class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    template_name = 'posts/post_create.html'
    fields = ['header_image', 'tags', 'category']
    success_url = reverse_lazy('all-posts')

    # def get(self, request):
    #     print(request.session['initial_form_data'])
    #     form = PostCreateForm()
        
    #     return render(request, 'posts/post_create.html', {'form': form})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 2 # Status set to Preview, instead of Publish
        # print(self.request.session['initial_form_data'])
        # print(form.cleaned_data)
        initial_data = form.save(commit = False)
        initial_data.title = self.request.session['title']
        initial_data.content = self.request.session['content']
        print(initial_data.header_image)
        initial_data.save()
        
        # form.cleaned_data = {**self.request.session['initial_form_data'], **form.cleaned_data }
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('all-posts')
    
    def get(self, request, pk):
        
        context = {}

        # Get post title and author. Author returns as interger because of ForeignKey
        post = get_object_or_404(Post.objects.filter(id=pk).values('title', 'author'))
        # Returns authors name to be used in template later on
        author_name =  get_object_or_404(CustomUser.objects.filter(id=post['author']).values_list('username', flat=True))

        context = {
            'post' : {
                'post_title' : post['title'],
                'post_author' : author_name, # No points of returning author's name to template
            }
        }

        if not self.request.user.username == author_name:
            raise PermissionDenied       

        return render(request, 'posts/post_delete.html', context=context)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    # fields = ['title', 'content', 'category']
    template_name = 'posts/post_update.html'
    form_class = PostUpdateForm

    def test_func(self):

        post_id = self.kwargs['pk']
        post_author_id = get_object_or_404(Post.objects.filter(id=post_id).values('author'))
        post_author_name =  get_object_or_404(CustomUser.objects.filter(id=post_author_id['author']).values_list('username', flat=True))

        if not self.request.user.username == post_author_name:
            return False
        return True