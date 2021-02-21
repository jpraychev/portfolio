from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
import re
from django.core.mail import send_mail

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
		# messages.success(self.request, 'You have registered successfully. You can now log in.')
        user = form.save()
        user.is_active = False
        user.save()
        return super().form_valid(form)

        # user.email holds the email
        send_mail(
            'Subject here',
            'Here is the message.',
            'jraychevdjango@gmail.com',
            [user.email],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('login'))

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = reverse_lazy('login')

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/profile_update.html'
    success_url ="/"

    def test_func(self):

        # get requested user from URL
        regex = re.compile('(/accounts/)(\w+)(/update)')
        m = regex.match(self.request.path)
        requested_user = m.group(2)
        
        if self.request.user.username == requested_user:
            return True
        return False

class LoginView(LoginView):
    template_name = 'accounts/login.html'

class LogoutView(RedirectView):

    template_name = 'accounts/logout.html'

    def get(self, request):
        return render(request, 'accounts/logout.html')
    
    def post(self, request):
        logout(request)
		# messages.success(request, 'You have successfully logged out. Log in <a href = ' + str(reverse_lazy('login')) + '> again</a>')
        return HttpResponseRedirect('/')


