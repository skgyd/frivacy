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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frivacyApp.views.login,name="login"),
    path('decEdit/',frivacyApp.views.decEdit,name="decEdit"),
    path('decNew/',frivacyApp.views.decNew,name="decNew"),
    path('notice/',frivacyApp.views.notice,name="notice"),
    path('declaration/',frivacyApp.views.declaration,name="declaration"),
    path('home/',frivacyApp.views.home,name="home"),
    path('signup/',frivacyApp.views.signup,name="signup"),
    path('detail/',frivacyApp.views.detail,name="detail"),
    path('edit/',frivacyApp.views.edit,name="edit"),
    path('new/',frivacyApp.views.new,name="new"),
    path('decDetail/',frivacyApp.views.decDetail,name="decDetail"),
    path('notDetail/',frivacyApp.views.notDetail,name="notDetail"),
    path('infoModify/',frivacyApp.views.infoModify,name="infoModify"),
    path('mypage/',frivacyApp.views.mypage,name="mypage"),
    url(r'signup/ajax-sign-up$',frivacyApp.views.ajaxsignup),
    url(r'^ajax-login$',frivacyApp.views.ajaxlogin),
    url(r'^logout$',frivacyApp.views.logout,name="logout"),
    url(r'^imageBlur$',frivacyApp.views.imageBlur),
    url(r'^imageUpload$',frivacyApp.views.imageUpload),
    url(r'^ajax-upload$',frivacyApp.views.ajaxupload),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)