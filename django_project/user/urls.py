from django.urls import path
from user import views
from django.contrib.auth import views as userview

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', userview.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', userview.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
