from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models, forms


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:profile')
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            profile = models.Profile()
            profile.first_name = form.cleaned_data['username']
            profile.user = request.user
            profile.save()
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )

            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})


@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    profile = get_object_or_404(models.Profile, pk=request.user.id)
    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = get_object_or_404(models.Profile, pk=request.user.id)
    form = forms.EditFormWithValidation(instance=profile)

    if request.method == 'POST':
        form = forms.EditFormWithValidation(request.POST, request.FILES,
                                            instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Updated {}'s profile".format(
                                 form.cleaned_data['first_name']))
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'edit.html',
                  {'form': form, 'profile': profile})


@login_required
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Password has been changed and you have been"
                " logged out for security purposes"
            )

            return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/change_password.html', {'form': form})
