from django.shortcuts import render
from django.views.generic import CreateView
from contact.models import Contact
from django.urls import reverse_lazy, reverse

class ContactView(CreateView):

    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact')