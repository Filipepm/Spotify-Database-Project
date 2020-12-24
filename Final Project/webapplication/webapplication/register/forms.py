from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	favoriteSong = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ["username", "favoriteSong", "password1", "password2"]