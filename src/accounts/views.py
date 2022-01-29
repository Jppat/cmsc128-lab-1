from django import forms
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from altaria.models import Post

# Create your views here.

User = get_user_model()

def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username= form.cleaned_data.get("username")
		password= form.cleaned_data.get("password1")
		#check if user details are valid
		try:
			user = User.objects.create_user(username=username, password=password)
			print(user)
		except:
			user = None
		if user != None:
			login(request, user)
			return redirect("/")
		else:
			request.session["register_error"] = 1
	return render(request,"register.html", {"form": form})

def login_view(request):
	if request.user.is_anonymous:
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username= form.cleaned_data.get("username")
			password= form.cleaned_data.get("password")
			#check if user details are valid
			user = authenticate(request, username=username, password=password)
			if user != None:
				request.session.set_expiry(10)
				login(request, user)
				return redirect("newspage")
			else:
				messages.error(request,"Wrong password.")
		return render(request,"login.html", {"form": form})
	else:
		return redirect("newspage")


def logout_view(request):
	logout(request)
	return render(request, "logout.html")