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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^decEdit$',views.decEdit,name="decEdit"),
    url(r'^decNew$',views.decNew,name="decNew"),
    url(r'^notice$',views.notice,name="notice"),
    url(r'^declaration$',views.declaration,name="declaration"),
    url(r'^login$',views.login,name="login"),
    url(r'^signup$',views.signup,name="signup"),
    url(r'^ajax-sign-up$',views.ajaxsignup),
    url(r'^ajax-login$',views.ajaxlogin),
    url(r'^logout$',views.logout,name="logout"),
    url(r'^imageBlur$',views.imageBlur),
    url(r'^imageUpload$',views.imageUpload),
    url(r'^mypage$', views.mypage, name="mypage"),
    url(r'^edit$',views.edit,name="edit"),
    url(r'^infoModify$',views.infoModify,name="infoModify"),
    url(r'^decDetail$',views.decDetail,name="decDetail"),
    url(r'^ajax-upload$',views.ajaxupload),
]


