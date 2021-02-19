from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class CustomUserChangeForm(UserChangeForm):

    # Removes password from user change form which is included by default
    password = None

    class Meta:
        model = CustomUser
        fields = ('department', 'profile_image',)