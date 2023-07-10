from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *


# signing up form for blog use
def sign_up(request):
    form = SignupForm()
    registered = False

    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True  # a message will pop up to let the user know that their registration was a success

    context = {
        'form': form,
        'registered': registered
    }

    return render(request, 'App_login/signup.html', context=context)


def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # authenticating
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # logging in
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))  # redirect to homepage after a user is logged in

    context = {'form': form}

    return render(request, 'App_login/login.html', context=context)


# logout function
@login_required  # user must be logged in to access this function
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))


# user profile page
@login_required
def profile_page(request):
    context = {}
    return render(request, 'App_login/profile.html', context=context)


# to allow user to edit their profile
@login_required
def edit_profile(request):
    current_user = request.user  # get the current logged in user
    form = UserProfileForm(instance=current_user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            form = UserProfileForm(instance=current_user)  # update info on page

    context = {'form': form}

    return render(request, 'App_login/edit_profile.html', context=context)


@login_required
def change_password(request):
    current_user = request.user  # get the current logged in user
    changed = False
    form = PasswordChangeForm(current_user)

    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)

        if form.is_valid():
            form.save()
            changed = True

    context = {'form': form,
               'changed': changed
               }

    return render(request, 'App_login/change_password.html', context)


@login_required
def add_profile_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)

        if form.is_valid():
            current_user = form.save(commit=False)
            current_user.user = request.user
            current_user.save()

            return HttpResponseRedirect(reverse('App_login:profile'))

    context = {'form': form}

    return render(request, 'App_login/profile_pic.html', context=context)


@login_required
def update_profile_pic(request):
    # this user already has a profile image so we need to access the instance of the user
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        # replacing image
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('App_login:profile'))  # return to profile page

    context = {'form': form}

    return render(request, 'App_login/profile_pic.html', context=context)
