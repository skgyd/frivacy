from django.shortcuts import render, redirect
from .models import User, Image
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as dlogout
from .detect_face_image import detecting

# Create your views here.

def home(request):
    context = {}
    if request.user.is_authenticated:
        u = User.objects.filter(userid=request.user.userid)[0]
        context = {'user': request.user, 'ProfilePic': u.profilepic}
        return render(request, 'home.html', context)
    return render(request,'login.html',context)

def decEdit(request):
    context = {}
    return render(request,'decEdit.html',context)

def notice(request):
    context = {}
    return render(request,'notice.html',context)

def declaration(request):
    context = {}
    return render(request,'declaration.html',context)
    
def decNew(request):
    context = {}
    return render(request,'decNew.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)

def signup(request):
    context = {}
    return render(request,'signup.html',context)

def logout(request):
    context = {}
    dlogout(request)
    return redirect(home)

def ajaxsignup(request):
    ajax = AjaxSignUp(request.POST)
    context = {'ajax_output': ajax.output()}
    return render(request,'ajax.html',context)

def ajaxlogin(request):
    ajax = AjaxLogin(request.POST)
    logged_in_user, output = ajax.validate()
    if logged_in_user != None:
        auth_login(request, logged_in_user)
    context = {'ajax_output': output}
    return render(request,'ajax.html',context)

def imageUpload(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Image.objects.last()
            src = 'img/' + str(img.image)
            if len(detecting(src))!=0:
                list = detecting(src).tolist()
                return render(request, 'imageBlur.html', {
                    'list': list,
                    'src': src
                })
            else:
                return render(request, 'imageBlur.html', {
                    'list': [],
                    'src': src
                })
    return render(request, 'imageUpload.html', locals())

def imageBlur(request):
    return render(request, 'imageBlur.html', locals())

