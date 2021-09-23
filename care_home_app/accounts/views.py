from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def sign_in(request):
    """Process the user login request"""
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
