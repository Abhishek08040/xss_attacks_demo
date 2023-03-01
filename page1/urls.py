from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/submit_comment', views.submit_comment, name="submit_comment"),

]
