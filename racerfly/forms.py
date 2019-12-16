from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'email', 'password', 'city']
		widgets = {
			'password': forms.PasswordInput(),
		}

class LoginForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['email', 'password']
		widgets = {
			'password': forms.PasswordInput(),
		}