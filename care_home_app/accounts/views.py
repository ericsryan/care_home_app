from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserChangeForm)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def sign_in(request):
    """Process the user login request."""
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    # messages.success(
                    #     request,
                    #     f"You are now logged in as {user.username}"
                    # )
                    return HttpResponseRedirect(reverse('index'))
                else:
                    messages.error(
                        request,
                        "That user account has been disabled"
                    )
            else:
                message.error(
                    request,
                    "The username or password is incorrect"
                )
    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def sign_out(request):
    """Log the user out of the site."""
    logout(request)
    # messages.success(request, "You've been logged out. Come back soon!")
    return HttpResponseRedirect(reverse('index'))


@login_required
def view_account(request):
    """Display the details of the user's account."""
    user = request.user
    return render(request, 'accounts/view_account.html', {'user': user})


@login_required
def edit_account(request):
    """Edit the details of a user's account."""
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated.")
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_account.html', {'form': form})
