from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):

	username 	= forms.CharField()
	password 	= forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username 	= self.cleaned_data.get("username")
		password 	= self.cleaned_data.get("password")

		if username and password:
			
			user = authenticate(username = username, password = password)

			if not user:
				if not User.objects.filter(username=username):
					raise forms.ValidationError("This username does not exist")

				if not User.objects.filter(password=username):
					raise forms.ValidationError("Incorrect password")

		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2'
		]
	email		= forms.EmailField()
	password1 	= forms.CharField(widget=forms.PasswordInput)
	password2 	= forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):

		username  = self.cleaned_data.get("username")
		email     = self.cleaned_data.get("email")
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if User.objects.filter(username=username):
			raise forms.ValidationError("This username already exists")

		if User.objects.filter(email=email):
			raise forms.ValidationError("This email address already exists")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")

		return super(UserRegisterForm, self).clean(*args, **kwargs)