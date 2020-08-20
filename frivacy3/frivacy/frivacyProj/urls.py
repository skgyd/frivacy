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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
import frivacyApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frivacyApp.views.login, name="login"),
    path('notice/', frivacyApp.views.notice, name="notice"),
    path('home/', frivacyApp.views.home, name="home"),
    path('signup/', frivacyApp.views.signup, name="signup"),
    path('infoModify/', frivacyApp.views.infoModify, name="infoModify"),
    path('mypage/', frivacyApp.views.mypage, name="mypage"),
    path('forgot/', frivacyApp.views.forgot, name="forgot"),
    path('forgotNext/', frivacyApp.views.forgotNext, name="forgotNext"),
    url(r'mypage/(?P<userid>[a-zA-Z0-9_]+)/$', frivacyApp.views.mypage),
    url(r'^modifyAct$', frivacyApp.views.modifyAct),
    url(r'signup/ajax-sign-up$', frivacyApp.views.ajaxsignup),
    url(r'^ajax-login$', frivacyApp.views.ajaxlogin),
    url(r'^logout$', frivacyApp.views.logout, name="logout"),
    url(r'^imageBlur$', frivacyApp.views.imageBlur),
    url(r'^imageUpload$', frivacyApp.views.imageUpload, name="imageUpload"),
    url(r'^ajax-upload$', frivacyApp.views.ajaxupload),
    url(r'detail/(?P<noticeid>[a-zA-Z0-9_]+)/$', frivacyApp.views.detail, name="detail"),
    url(r'edit/(?P<postid>[a-zA-Z0-9_]+)/$', frivacyApp.views.edit, name="edit"),
    url(r'delete/(?P<postid>[a-zA-Z0-9_]+)/$', frivacyApp.views.delete, name="delete"),
    path('followAct/', frivacyApp.views.followAct, name="followact"),
    url(r'followAct/(?P<userid>[a-zA-Z0-9_]+)/$', frivacyApp.views.followAct),
    url(r'unfAct/(?P<userid>[a-zA-Z0-9_]+)/$', frivacyApp.views.unfAct),
    url(r'^commentAct$', frivacyApp.views.commentAct),
    url(r'^findAct$', frivacyApp.views.findAct),
    url(r'^findNextAct$', frivacyApp.views.findNextAct),
    url(r'report/(?P<postid>[a-zA-Z0-9_]+)/(?P<reportid>[a-zA-Z0-9_]+)/$', frivacyApp.views.report),
    url(r'likeAct/(?P<postid>[a-zA-Z0-9_]+)/$', frivacyApp.views.likeAct),
    url(r'likeDelAct/(?P<postid>[a-zA-Z0-9_]+)/$', frivacyApp.views.likeDelAct),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
