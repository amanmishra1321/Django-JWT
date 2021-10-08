from django.contrib import admin
from django.urls import path
from Users import views
urlpatterns = [
    path('signup/', views.RegisterView.as_view()),
    path('login/',views.LoginView.as_view()),
]
