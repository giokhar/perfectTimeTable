from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
	return render(request, 'login.html')

# @login_required(login_url='/login/')
def admin(request):
	return render(request, 'index.html')