from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseForbidden
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile
from accounts.forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserForm,
    ProfileForm
)


@login_required
def logout(request):
    """Logout the user and return index page"""

    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""

    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in!')
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, 
                    'Your username or password is incorrect!'
                )
    else:
        login_form = UserLoginForm()

    context = {
        'login_form': login_form,
        'login_page': 'active',
        'title': 'Login'
    }
    return render(request, 'login.html', context)

def register(request):
    """ A view that manages the registration form"""

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return redirect('index')
            else:
                messages.error(request, 'Unable to log you in at this time!')
    else:
        user_form = UserRegistrationForm()
    context = {
        'user_form': user_form,
        'register_page': 'active',
        'title': 'Register'
    }
    return render(request, 'register.html', context)

def user_profile(request):
    """Fetch the user data and the linked profile data."""

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user is not None):
                user = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            return redirect('accounts:register')
    context = {
        'user': user,
        'profile_page': 'active',
        'title': 'Profile'
    }
    return render(request, 'profile.html', context)

@transaction.atomic
def update_profile(request):
    """
    Fetch data from user and user profile and render it on the form.
    Update both models.
    """

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profiles)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, ('Your profile has been updated successfully!'))
                return redirect('user_profile')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profiles)
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
                'title': 'Update',
                'profile': 'profile'
            }
            return render(request, 'update_profile.html', context)