from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

def view_article(request):
	# user = request.session.user
	if not request.user.is_anonymous:
		post_object = Post.objects.first()
		context = {
		'post_object': post_object
		}
		return render(request, "index.html", context)
	else:
		return redirect("logout")


def guest_view(request):
	if request.user.is_anonymous:
		post_object = Post.objects.first()
		context = {
		'post_object': post_object
		}
		return render(request, "index.html", context)
	else:
		return redirect("newspage")