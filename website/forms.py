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
