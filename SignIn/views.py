from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
import datetime
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# view for homepage of the website which deals with user-login
def home(request):
    return render(request, "SignIn/index.html", {'title': "Login"})


# view for sign-in page for new users
def signin(request):

    # if the user submits the sign-in form
    if request.method == 'POST':

        # create a form with details as in request.POST
        form = UserCreationForm(request.POST)
        if form.is_valid():

            # save the form with encrypted password
            form.save()
            username = form.cleaned_data.get('username')

            # message to be displayed in the next page to show the signin process was successful
            messages.success(
                request, f'Your account has been created! You are now able to log in')

            # redirect to the login page()
            return redirect('SignIn:login')
    else:
        form = UserCreationForm()
    context = {'form': form, 'title': "Sign-in"}
    return render(request, "SignIn/signin.html", context)
