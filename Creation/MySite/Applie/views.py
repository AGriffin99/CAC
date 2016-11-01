from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request, 'Homepage.html', {})
def signup(request):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username= form.save(commit=False)
            username.set_password(username.password)
            # username.password = make_password(form.cleaned_data['password'])
            # username.status=1
            username.save()
            print(request.POST)
            return profilepage(request)
        else:
            return render(request,'signup.html',{"form":form})
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # username = request.POST['username']
            # password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(password)
            # check_password()
            if user is not None:
                login(request, user)
                # user_logged_in
                return Homepage(request)
            else:
                message = "Your password is incorrect. Try again!"
                # return login(request, form)
                return retry_login(request, message)


        else:
            # return login(request, form)
            return retry_login(request)
    else:
        return retry_login(request)

def retry_login(request, message=None):
    form = UserLoginForm()
    return render(request, 'login.html', {"form":form, "message":message})
