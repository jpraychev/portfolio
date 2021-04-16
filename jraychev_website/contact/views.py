from django.shortcuts import render
from django.views.generic import CreateView, FormView
from contact.models import Contact
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.mail import send_mail
from django.conf import settings

def send_email(form_data, remote_ip):

    form_message = form_data.cleaned_data['message']
    subject = form_data.cleaned_data['subject']
    
    try:
        email = form_data.cleaned_data['email']
    except:
        email = 'INVALID EMAIL'
        
    message = f'''The current message was received from {email} with IP: {remote_ip}
    
    {form_message}
    '''

    send_mail(subject, 
        message, 
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=[settings.ADMIN_EMAIL], 
        fail_silently=False) 


class ContactView(SuccessMessageMixin, CreateView):

    # model = Contact
    # fields = ['name', 'email', 'subject', 'message']
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact/contact.html'
    # success_message = "Your message was submitted successfully!"

    def form_invalid(self, form):

        remote_ip = self.request.META.get('REMOTE_ADDR')
        send_email(form, remote_ip)

        messages.error(self.request, 'Something went wrong with your submission. Please try again.')
        return HttpResponseRedirect('')

    def form_valid(self, form):

        remote_ip = self.request.META.get('REMOTE_ADDR')
        send_email(form, remote_ip)

        messages.success(self.request, 'Your message was submitted successfully!')
        return super().form_valid(form)