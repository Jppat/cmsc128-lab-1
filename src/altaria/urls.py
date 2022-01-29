from django.urls import path, include
from altaria import views
from accounts import views as account_views

urlpatterns = [
	path('', account_views.login_view, name='landingpage'),
	# path('login/', account_views.login_view, name='loginpage'),
	path('newspage/', views.view_article, name='newspage'),
	path('guest/', views.guest_view, name='guest'),
	path('logout/', account_views.logout_view, name= 'logout'),
	path('register/', account_views.register_view, name= 'register'),
]