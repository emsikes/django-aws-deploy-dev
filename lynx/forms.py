# User registation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

# User login

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, FileInput
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# profile management update
class UpdateUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
        exlude = ['password1', 'password2']

# Update profile model
class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['profile_pic']
        