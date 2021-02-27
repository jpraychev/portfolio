from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView, UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
import re
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

def username_valid(username):

    invalid_characters = re.compile('(?![a-zA-Z0-9.@_]).')
    valid_email = re.compile(r'(^[\w\-\.]+@[\w]+\.[\w]{1,5}$)')

    if not invalid_characters.search(username):
        if re.match(valid_email, username):
            return True
    return False

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

        # get requested user from URL using regex - OLD - can be removed
        # regex = re.compile('(/accounts/)(\w+)(/update)')
        # m = regex.match(self.request.path)
        # requested_user = m.group(2)
        
        requested_user = self.kwargs['slug']

        if not self.request.user.username == requested_user:
            return False
        return True

class LoginView(LoginView):

    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):

        form = self.form_class(request, request.POST)

        username = request.POST['username']
        password = request.POST['password']

        # Username custom validation
        if not username_valid(username): 
            print('Username validation failed. Redirecting...')
            return render(request, self.template_name, {'form': form})

        current_user = CustomUser.objects.filter(email=username).values_list('username', flat=True)

        if current_user:
            get_user = get_object_or_404(current_user)
            user = authenticate(username=get_user, password=password)
        else:
            print('User does no exists')
            return render(request, self.template_name, {'form': form})

        if user is not None:
            if user.is_active:
                login(request, user)
                if (self.request.GET.get('next') is None):
                    # messages.success(request, 'You have successfully logged in.')
                    return HttpResponseRedirect('/')
                else:
                    # messages.success(request, 'You have successfully logged in.')
                    return HttpResponseRedirect(self.request.GET.get('next'))
            else:
                # messages.error(request, 'Something went wront. Contact the system administrator!')
                return HttpResponseRedirect('/')
        else:
            # messages.error(request, 'Something went wront. Contact the system administrator!')
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

class LogoutView(RedirectView):

    template_name = 'accounts/logout.html'

    def get(self, request):
        return render(request, 'accounts/logout.html')
    
    def post(self, request):
        logout(request)
		# messages.success(request, 'You have successfully logged out. Log in <a href = ' + str(reverse_lazy('login')) + '> again</a>')
        return HttpResponseRedirect('/')


