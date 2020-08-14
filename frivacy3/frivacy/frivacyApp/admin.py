from django.contrib import admin
from .models import User, Post, Image

# Register your models here.

class UserAdmin(admin.ModelAdmin) :
    list_display = ('userid', 'name', 'email', 'password', 'sign_up_date', 'profilepic')

class PostAdmin(admin.ModelAdmin):
    list_display = ('image', 'owner', 'content', 'date_uploaded')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(User, UserAdmin) #site에 등록
admin.site.register(Post, PostAdmin) #site에 등록
admin.site.register(Image, ImageAdmin) #site에 등록