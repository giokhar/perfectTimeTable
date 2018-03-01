from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required

from website.forms import UserLoginForm, UserRegisterForm

from website.dashboard import Dashboard
from minConflict.models import Student

# Create your views here.

def index_view(request):
	return render(request, 'home.html')

@login_required(login_url='/login')
def dashboard_view(request):

	dashboard = Dashboard(request.user)

	if dashboard.isAdmin:
		return render(request, 'staff/admin.html', {"dashboard": dashboard})

	return render(request, 'dashboard.html', {"dashboard": dashboard})


def login_view(request):
	""" log in user controller"""

	# If user is already logged in it should automatically redirect to the dashboard
	if request.user.is_authenticated():
		return redirect('dashboard')

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

	# If user is already logged in it should automatically redirect to the dashboard
	if request.user.is_authenticated():
		return redirect('dashboard')

	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password1')
		user.set_password(password)
		user.save()

		# Creating instance in the Students table
		email 		= form.cleaned_data.get("email")
		semester 	= form.getSemester()

		new_student = Student(email = email, semester = semester)
		new_student.save()

		login(request, user, backend='django.contrib.auth.backends.ModelBackend')
		return redirect('dashboard')

	return render(request, 'register.html', {"form": form})

def logout_view(request):
	""" log out user controller"""

	# If user is already logged in it should automatically redirect to the dashboard
	if request.user.is_authenticated():
		logout(request)
	
	return redirect('index')