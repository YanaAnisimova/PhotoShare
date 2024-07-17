from django.contrib import admin

from user_auth.models import User


admin.site.register(User)


# from django import forms
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from users.models import CustomUser
#
#
# class UserCreationForm(forms.ModelForm):
#     """
#     A form for creating new users. Includes all the required fields."""
#
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#
#     class Meta:
#         model = CustomUser
#         fields = ["email", "first_name", "last_name", "groups", "organization"]
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     model = CustomUser
#     ordering = ["email"]
#     search_fields = ["email"]
#     list_display = ["email", "first_name", "last_name", "organization", "is_staff"]
#
#     # for fields to be used when creating a user
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["email", "first_name", "last_name", "groups", "password", "organization"],
#             },
#         ),
#     ]
#
#     # for fields to be used in editing users
#     fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["email", "first_name", "last_name", "groups", "organization"],
#             },
#         ),
#     ]
#
#
# admin.site.register(CustomUser, CustomUserAdmin)


