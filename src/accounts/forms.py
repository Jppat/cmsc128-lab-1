import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class RegisterForm(forms.Form):
	username = forms.CharField()
	password1 = forms.CharField(
		label = "Password",
		widget =forms.PasswordInput(
			attrs={
				"id" : "user-password1"
			}
		)
	)
	password2 = forms.CharField(
		label = "Confirm Password",
		widget =forms.PasswordInput(
			attrs={
				"id" : "user-password2"
			}
		)
	)

	def clean(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username__iexact=username)
		errors = []
		if qs.exists():
			errors.append(forms.ValidationError("Username already exists. Please pick another one."))
		if password1 != password2:
			errors.append(forms.ValidationError("Password confirmation did not match. Please try again. "))
		if len(password1) < 8:
			errors.append(forms.ValidationError("Your password must be at least 8 characters long. "))
		if len(re.findall("[A-Z]",password1)) < 1:
			errors.append(forms.ValidationError("Your password must have at least 1 capital letter. "))
		if len(re.findall("[0-9]",password1)) < 1:
			errors.append(forms.ValidationError("Your password must have at least 1 numeric character. "))
		if len(re.findall("[^A-Za-z0-9]",password1)) < 1:
			errors.append(forms.ValidationError("Your password must have at least 1 special character. "))
		if errors:
			raise forms.ValidationError(errors)

		


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"id" : "user-password"
			}
		)
	)


	def clean_username(self):
		errors = []
		username= self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if not qs.exists():
			errors.append(forms.ValidationError("Username does not exist. Please register first. "))
		if errors:
			raise forms.ValidationError(errors)
		return username