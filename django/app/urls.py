from django.urls import  path

from app import views

urlpatterns = [
    path('', views.home),
    path('register/', views.registerPage),

    path('login/', views.loginPage),
 ]