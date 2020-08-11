from django import forms
from .models import Image

# html에서 form을 쓰기 위해 생성한 것
class UploadDocumentForm(forms.Form):
    image = forms.ImageField()

# model의 이미지와 db를 연동하기 위한 것 (query 셋 만들어줌)
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']