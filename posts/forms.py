from django import forms

class PostCreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=True)
    content = forms.CharField(label='Content', required=True)