from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

from website.forms import UserLoginForm

# Create your views here.

def index_view(request):
	return render(request, 'index.html')

def login_view(request):
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		email 		= form.cleaned_data.get("email")
		password 	= form.cleaned_data.get("password")

	return render(request, 'login.html', {"form": form})

def register_view(request):
	return render(request, 'register.html')

def logout_view(request):
	return render(request, 'login.html')

def dashboard_view(request):
	return render(request, 'index.html')