from django import forms
from django.contrib.auth import authenticate
from django.db.models import F
from .models import Image, Post, Profile
from django.contrib.auth.hashers import make_password, check_password
from urllib.request import urlopen
from random import randint
import base64
import os
from django.contrib.auth.models import User
import json, re

class Ajax(forms.Form):
    args = []
    user = []

    def __init__(self, *args, **kwargs):

        self.args = args
        if len(args) > 1:
            self.user = args[1]
            if self.user.id == None:
                self.user = "NL"

    def error(self, message):
        return json.dumps({"Status": "Error", "Message": message}, ensure_ascii=False)

    def success(self, message):
        return json.dumps({"Status": "Success", "Message": message}, ensure_ascii=False)

    def items(self, json):
        return json

    def output(self):
        return self.validate()

class AjaxSignUp(Ajax):
    
    def validate(self):
        try:
            self.userid = self.args[0]["id"]
            self.password = self.args[0]["pw"]
            self.password2 = self.args[0]["pw2"]
            self.email = self.args[0]["email"]
            self.name = self.args[0]["name"]
            self.a1 = self.args[0]["a1"]
            self.a2 = self.args[0]["a2"]
        except Exception as e:
            return self.error("Malformed request, did not process.")

        if not re.match('^[a-zA-Z0-9_]+$', self.userid):
            return self.error("아이디는 알파벳과 숫자만으로 구성되어야 합니다")
        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            return self.error("올바르지 않은 이메일 형식입니다")
        if len(self.userid) < 4 or len(self.userid) > 20:
            return self.error("아이디는 4자에서 20자 사이여야 합니다")
        if self.password != self.password2:
            return self.error("비밀번호가 일치하지 않습니다")
        if len(self.password) < 6 or len(self.password) > 32:
            return self.error("비밀번호는 6자에서 32자 사이여야 합니다")
        if len(self.email) < 6 or len(self.email) > 140:
            return self.error("이메일은 6자에서 32자 사이여야 합니다")

        if User.objects.filter(username=self.userid).exists():
            return self.error("이미 사용하고 있는 아이디입니다")

        if User.objects.filter(email=self.email).exists():
            return self.error("이미 사용하고 있는 이메일입니다")

        u = User(username=self.userid, password=make_password(self.password), email=self.email, first_name=self.name)
        u.save()
        p = Profile(username=self.userid, image="", a1=self.a1, a2=self.a2)
        p.save()
        return self.success("Account Created!")

# html에서 form을 쓰기 위해 생성한 것
class UploadDocumentForm(forms.Form):
    image = forms.ImageField()

# model의 이미지와 db를 연동하기 위한 것 (query 셋 만들어줌)
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image'] 
