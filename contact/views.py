from django.shortcuts import render
from django.views.generic import CreateView, FormView
from contact.models import Contact
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect

class ContactView(SuccessMessageMixin, CreateView):

    # model = Contact
    # fields = ['name', 'email', 'subject', 'message']
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact/contact.html'
    success_message = "Your message was submitted successfully!"

    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong with your submission. Please try again.')
        return HttpResponseRedirect('')

    # def form_valid(self, form):
    #     return super().form_valid(form)