from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):

    name = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label = '', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(label = '',  widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(
        label = '', 
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')