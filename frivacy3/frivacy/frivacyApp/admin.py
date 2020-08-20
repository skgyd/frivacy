from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'image')

class PostAdmin(admin.ModelAdmin):
    list_display = ('image', 'owner', 'content', 'date_uploaded', 'likes')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'date_uploaded')

class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'follower')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('postid', 'user', 'comment', 'date_uploaded')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('postid', 'type0', 'type1', 'type2', 'type3', 'type4', 'type5', 'total')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('postid', 'liker')

admin.site.register(Profile, ProfileAdmin) #site에 등록
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Follower, FollowerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Like, LikeAdmin)