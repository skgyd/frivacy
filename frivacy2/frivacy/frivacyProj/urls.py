"""frivacyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import frivacyApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frivacyApp.views.home,name="home"),
    path('decEdit/',frivacyApp.views.decEdit,name="decEdit"),
    path('decNew/',frivacyApp.views.decNew,name="decNew"),
    path('notice/',frivacyApp.views.notice,name="notice"),
    path('declaration/',frivacyApp.views.declaration,name="declaration"),
    path('login/',frivacyApp.views.login,name="login"),
    path('signup/',frivacyApp.views.signup,name="signup"),
]
