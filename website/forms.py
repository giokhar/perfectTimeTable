from django import forms


class UserLoginForm(forms.Form):

	email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)