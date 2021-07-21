from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handleSignup, name="handleSignup"),
    path('login',views.handleLogin, name="handleLogin"),
    
    path('logout',views.handleLogout, name="handleLogout"),
    path('notes',views.notes, name="notes"),
    path('assignments',views.assignments, name="assignments"),
    path('questions',views.questions, name="questions"),
    path('about',views.about,name="about"),
    
    
]