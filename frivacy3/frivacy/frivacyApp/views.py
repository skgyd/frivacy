from django.shortcuts import render, redirect
from .models import User, Image
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as dlogout
from .detect_face_image import detecting
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def home(request):
    context = {}
    u = request.session.get('user')
    if u:
        u2 = User.objects.filter(userid=u)[0]
        if u2.profilepic == "":
            u2.profilepic = "static/img/default.png"
        context = {'user': u, 'ProfilePic': u2.profilepic, 'name': u2.name}
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
    request.session.pop('user')
    return redirect(home)

def ajaxsignup(request):
    ajax = AjaxSignUp(request.POST)
    context = {'ajax_output': ajax.output()}
    return render(request,'ajax.html',context)

def ajaxlogin(request):
    context = {}
    if request.method == "POST":
        iid = request.POST.get('id', None)
        pw = request.POST.get('pw', None)

        if not (iid and pw):
            context['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            if not User.objects.filter(userid=iid).exists():
                context['error']="아이디나 비밀번호가 일치하지 않습니다"
            if not check_password(pw, User.objects.filter(userid=iid)[0].password):
                context['error']="아이디나 비밀번호가 일치하지 않습니다"
            else:
                u = User.objects.filter(userid=iid)[0]
                request.session['user'] = u.userid
                return redirect('/home')

        return render(request, 'login.html', context)

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
    context = {}
    if request.user.is_authenticated:
        u = User.objects.filter(userid=request.user.userid)[0]
        if u.profilepic == "":
            u.profilepic = "static/img/default.png"
        context = {'user': request.user, 'ProfilePic': u.profilepic}
    return render(request, 'imageBlur.html', context)

def mypage(request):
    return render(request,'mypage.html')

def edit(request):
    return render(request,'edit.html')

def infoModify(request):
    return render(request,'infoModify.html')

def decDetail(request):
    return render(request,'decDetail.html')

def ajaxupload(request):
    ajax = AjaxUpload(request.POST)
    context = {'ajax_output': ajax.output()}
    return render(request,'ajax.html',context)
    
def detail(request):
    return render(request,'detail.html')
    
def new(request):
    return render(request,'new.html')

def edit(request):
    return render(request,'edit.html')

def decDetail(request):
    return render(request,'decDetail.html')

def notDetail(request):
    return render(request,'notDetail.html')

def infoModify(request):
    return render(request,'infoModify.html')

def mypage(request):
    return render(request,'mypage.html')