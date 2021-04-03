from django import forms
from django.forms import ModelForm
from posts.models import Post

class PostCreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea, label='Content', required=True)

class PostUpdateForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags')