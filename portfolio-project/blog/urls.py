from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='blog_index'),
    path('<int:blog_id>/', views.details, name='detail'),
]