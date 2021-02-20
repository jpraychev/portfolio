from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id', 'email', 'username', 'first_name','last_name','department', 'slug', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('department', 'slug', 'profile_image',)}),
    )

    
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('department', 'slug', 'profile_image',)}),
    )

    # Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)