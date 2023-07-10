from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


# personalising the default django user sign up form to my liking
class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# to allow user to edit profile
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


# for updating profile picture
class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
