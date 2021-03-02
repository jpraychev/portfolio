from django.shortcuts import render
from django.views.generic import CreateView
from contact.models import Contact
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

class ContactView(SuccessMessageMixin, CreateView):

    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    template_name = 'contact/contact.html'
    success_message = "Your message was submitted successfully!"
    success_url = reverse_lazy('contact')