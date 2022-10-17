from unicodedata import name
from django.urls import path
from blog import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('gadgets/',views.gadgets, name='gadgets'),
    path('contact/', views.contact, name='contact'),
    path('post/create/', views.createpost, name='post'),
    path('update/post/<str:pk>/', views.updatepost, name='updatepost'),
    path('delete/post/<str:pk>/', views.deletepost, name='deletepost'),
]
