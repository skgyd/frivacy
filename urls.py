from django.contrib import admin
from django.urls import path
import crudapp.views

urlpatterns = [
    path('login/', crudapp.views.new, name='login')
]
