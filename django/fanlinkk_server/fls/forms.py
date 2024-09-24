from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Model, User

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'email']

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and password.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'role')  # Include any additional fields you require

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on the user.
    """

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'username', 'role', 'is_active', 'is_staff')  # Include any additional fields you require
