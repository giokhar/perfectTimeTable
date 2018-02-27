from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required

from website.forms import UserLoginForm, UserRegisterForm

# Create your views here.

def index_view(request):
	return render(request, 'home.html')

@login_required(login_url='/login')
def dashboard_view(request):
	return render(request, 'dashboard.html')


def login_view(request):
	""" log in user controller"""

	next_page = request.GET.get("next")

	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username	= form.cleaned_data.get("username")
		password 	= form.cleaned_data.get("password")

		user = authenticate(username = username, password = password)
		login(request, user)
		# print(request.user.is_authenticated())

		if next_page:
			return redirect(next_page)

		return redirect('dashboard')

	return render(request, 'login.html', {"form": form})

def register_view(request):
	# print(request.user.is_authenticated())
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password1')
		user.set_password(password)
		user.save()
		login(request, user, backend='django.contrib.auth.backends.ModelBackend')
		return redirect('dashboard')

	return render(request, 'register.html', {"form": form})

@login_required(login_url='/login')
def logout_view(request):
	""" log out user controller"""
	logout(request)
	return redirect('index')