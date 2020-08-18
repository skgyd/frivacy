from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as dlogout
from .detect_face_image import detecting
from django.contrib.auth.hashers import make_password, check_password
import base64
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {}
    if request.user.is_authenticated:
        try:
            p = Profile.objects.filter(username=request.user.username)[0]
            if p.image == "":
                p.image = "img/default.png"
        except:
            return render(request,'login.html',context)

        # 나와 내가 팔로우하는 사람들의 게시글 가져오기
        out = []
        followerslist = [request.user.username]
        profilepics = {}

        for follower in Follower.objects.filter(follower=request.user.username):
            followerslist.append(follower.user)

        for user in Profile.objects.filter(username__in=followerslist):
            profilepics[user.username] = user.image
            if user.image == "":
                profilepics[user.username] = "img/default.png"
        for item in Post.objects.filter(owner__in=followerslist).order_by('-date_uploaded'):
            out.append(
                {"PostID": item.id, "URL": item.image, "Content": item.content, "Owner": item.owner,
                 "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                 "ProfilePic": profilepics[item.owner]})
        context = {'user': request.user, 'ProfilePic': p.image, 'posts':out}
        
        return render(request, 'home.html', context)
    return render(request,'login.html',context)

def decEdit(request):
    context = {}
    return render(request,'decEdit.html',context)

def notice(request):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        out = []
        cnt = 0
        for item in Notice.objects.all().order_by('-date_uploaded'): #공지사항 가져오기
            cnt = cnt+1
            out.append(
                {"NoticeID": item.id, "Content": item.content, "Owner": item.owner,
                 "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                 "Title": item.title})
        context = {'user': request.user, 'ProfilePic': p.image, 'posts':out, 'cnt':cnt}
        return render(request,'notice.html',context)
    return render(request,'login.html',context)

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

def forgot(request):
    context = {}
    return render(request,'forgot.html',context)

def logout(request):
    context = {}
    dlogout(request)
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
            return render(request, 'login.html', context)
        else : 
            if not User.objects.filter(username=iid).exists():
                context['error']="아이디나 비밀번호가 일치하지 않습니다"
                return render(request, 'login.html', context)
            if not check_password(pw, User.objects.filter(username=iid)[0].password):
                context['error']="아이디나 비밀번호가 일치하지 않습니다"
                return render(request, 'login.html', context)
            else:
                u = User.objects.filter(username=iid)[0]
                if u != None:
                    auth_login(request, u)
                return redirect('/home')

        return render(request, 'login.html', context)

def imageUpload(request):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        form = UploadDocumentForm()
        if request.method == 'POST': #이미지 업로드
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                img = Image.objects.last()
                src = 'img/' + str(img.image)
                if len(detecting(src))!=0:
                    list = detecting(src).tolist()
                    return render(request, 'imageBlur.html', {
                        'user': request.user,
                        'ProfilePic': p.image,
                        'list': list,
                        'src': src
                    })
                else:
                    return render(request, 'imageBlur.html', {
                        'user': request.user,
                        'ProfilePic': p.image,
                        'list': [],
                        'src': src
                    })
        return render(request, 'imageUpload.html', locals())
    return render(request,'login.html',context)

def imageBlur(request):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        context = {'user': request.useru, 'ProfilePic': p.image}
        return render(request, 'imageBlur.html', context)
    return render(request,'login.html',context)

def mypage(request, userid):
    context = {}
    if request.user.is_authenticated:
        try:
            p = Profile.objects.filter(username=userid)[0]
            if p.image == "":
                p.image = "img/default.png"
        except:
            context['error'] = "존재하지 않는 사용자입니다."
            return render(request,'home.html',context)
        if request.method == 'GET':
            out = [] #게시물
            profilepics = {}
            cnt = 0 #게시물 개수
            
            followerlist=[] #팔로워 리스트
            fercnt = 0 #팔로워 수
            followlist=[] #팔로우 리스트
            fcnt = 0 #팔로우 수
            flag = 1
            
            #userid가 쓴 post들 조회
            user = Profile.objects.filter(username=userid)[0]
            profilepics[user.username] = user.image
            if user.image == "":
                profilepics[user.username] = "img/default.png"
            for item in Post.objects.filter(owner=userid).order_by('-date_uploaded'):
                cnt = cnt+1
                out.append(
                    {"PostID": item.id, "URL": item.image, "Content": item.content, "Owner": item.owner,
                    "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                    "ProfilePic": profilepics[item.owner]})

            #userid의 팔로워 조회
            for f in Follower.objects.filter(user=userid):
                fercnt = fercnt+1
                fpic = Profile.objects.filter(username=f.follower)[0]
                if fpic.image == "":
                    fpic.image = "img/default.png"
                followerlist.append({"User": f.follower, "ProfilePic": fpic.image})
                if f.follower == request.user.username:
                    flag = 0

            #userid가 팔로우 하는 사용자 조회
            for f in Follower.objects.filter(follower=userid):
                fcnt = fcnt+1
                fpic = Profile.objects.filter(username=f.user)[0]
                if fpic.image == "":
                    fpic.image = "img/default.png"
                followlist.append({"User": f.user, "ProfilePic": fpic.image})

            u = User.objects.filter(username=userid)[0]
            suser = {"username":u.username, "first_name":u.first_name}
            context = {'user': request.user, 'ProfilePic': p.image, 'posts':out, 'suser': suser, 'cnt':cnt, 'fercnt':fercnt, 'fcnt':fcnt, 'follower':followerlist, 'follow':followlist, 'flag': flag}
            return render(request,'mypage.html', context)

    return render(request,'login.html',context)

def edit(request, postid):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        if request.method == 'POST':
            # 포스트 수정
            pid = request.POST.get('id', None)
            content = request.POST.get('content', None)
            
            post_instance = Post.objects.get(id=pid)
            post_instance.content = content
            post_instance.save()

            out = [] #게시물
            profilepics = {}
            cnt = 0 #게시물 개수
            
            followerlist=[] #팔로워 리스트
            fercnt = 0 #팔로워 수
            followlist=[] #팔로우 리스트
            fcnt = 0 #팔로우 수
            flag = 1
            
            #내가 쓴 post들 조회
            user = Profile.objects.filter(username=request.user)[0]
            profilepics[user.username] = user.image
            if user.image == "":
                profilepics[user.username] = "img/default.png"
            for item in Post.objects.filter(owner=request.user).order_by('-date_uploaded'):
                cnt = cnt+1
                out.append(
                    {"PostID": item.id, "URL": item.image, "Content": item.content, "Owner": item.owner,
                    "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                    "ProfilePic": profilepics[item.owner]})

            #userid의 팔로워 조회
            for f in Follower.objects.filter(user=request.user):
                fercnt = fercnt+1
                fpic = Profile.objects.filter(username=f.follower)[0]
                if fpic.image == "":
                    fpic.image = "img/default.png"
                followerlist.append({"User": f.follower, "ProfilePic": fpic.image})
                if f.follower == request.user.username:
                    flag = 0

            #userid가 팔로우 하는 사용자 조회
            for f in Follower.objects.filter(follower=request.user):
                fcnt = fcnt+1
                fpic = Profile.objects.filter(username=f.user)[0]
                if fpic.image == "":
                    fpic.image = "img/default.png"
                followlist.append({"User": f.user, "ProfilePic": fpic.image})

            u = User.objects.filter(username=request.user)[0]
            suser = {"username":u.username, "first_name":u.first_name}
            context = {'user': request.user, 'ProfilePic': p.image, 'posts':out, 'suser': suser, 'cnt':cnt, 'fercnt':fercnt, 'fcnt':fcnt, 'follower':followerlist, 'follow':followlist, 'flag': flag}
            return render(request,'mypage.html', context)
        else: # 수정 페이지 로드
            out = []
            item = Post.objects.filter(id=postid)[0]
            out.append({"PostID": item.id, "URL": item.image, "Content": item.content, "Owner": item.owner})
            context = {'user': request.user, 'ProfilePic': p.image, 'posts':out}
            return render(request,'edit.html',context)
    return render(request,'login.html',context)

def delete(request, postid):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        # 게시글 삭제
        Post.objects.get(id=postid).delete()
        #내가 쓴 글 불러오고 mypage로 다시 이동
        out = [] #게시물
        profilepics = {}
        cnt = 0 #게시물 개수
            
        followerlist=[] #팔로워 리스트
        fercnt = 0 #팔로워 수
        followlist=[] #팔로우 리스트
        fcnt = 0 #팔로우 수
        flag = 1
            
        #userid가 쓴 post들 조회
        user = Profile.objects.filter(username=request.user)[0]
        profilepics[user.username] = user.image
        if user.image == "":
            profilepics[user.username] = "img/default.png"
        for item in Post.objects.filter(owner=request.user).order_by('-date_uploaded'):
            cnt = cnt+1
            out.append(
                {"PostID": item.id, "URL": item.image, "Content": item.content, "Owner": item.owner,
                "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                "ProfilePic": profilepics[item.owner]})

        #userid의 팔로워 조회
        for f in Follower.objects.filter(user=request.user):
            fercnt = fercnt+1
            fpic = Profile.objects.filter(username=f.follower)[0]
            if fpic.image == "":
                fpic.image = "img/default.png"
            followerlist.append({"User": f.follower, "ProfilePic": fpic.image})
            if f.follower == request.user.username:
                flag = 0

        #userid가 팔로우 하는 사용자 조회
        for f in Follower.objects.filter(follower=request.user):
            fcnt = fcnt+1
            fpic = Profile.objects.filter(username=f.user)[0]
            if fpic.image == "":
                fpic.image = "img/default.png"
            followlist.append({"User": f.user, "ProfilePic": fpic.image})

        u = User.objects.filter(username=request.user)[0]
        suser = {"username":u.username, "first_name":u.first_name}
        context = {'user': request.user, 'ProfilePic': p.image, 'posts':out, 'suser': suser, 'cnt':cnt, 'fercnt':fercnt, 'fcnt':fcnt, 'follower':followerlist, 'follow':followlist, 'flag': flag}
        return render(request,'mypage.html', context)
    return render(request,'login.html',context)

def infoModify(request):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        context = {'user': request.user, 'ProfilePic': p.image}
        return render(request,'infoModify.html', context)
    return render(request,'login.html',context)

def modifyAct(request):
    context = {}
    if request.user.is_authenticated:
        try:
            p = Profile.objects.filter(username=request.user)[0]
            if p.image == "":
                p.image = "img/default.png"
        except:
            return render(request,'login.html',context)
        context = {'user': request.user, 'ProfilePic': p.image}
        if request.method == "POST":
            #개인정보 업데이트
            userid = request.POST.get('id', None)
            password = request.POST.get('pw', None)
            password2 = request.POST.get('pw2', None)
            email = request.POST.get('email', None)
            name = request.POST.get('name', None)
            profilepic = request.FILES.get('image','')

            if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                context['error']="올바르지 않은 이메일 형식입니다"
                return render(request,'infoModify.html', context)
            if password != password2:
                context['error']="비밀번호가 일치하지 않습니다"
                return render(request,'infoModify.html', context)
            if password != "":
                if len(password) < 6 or len(password) > 32:
                    context['error']="비밀번호는 6자에서 32자 사이여야 합니다"
                    return render(request,'infoModify.html', context)
            if len(email) < 6 or len(email) > 140:
                context['error']="이메일은 6자에서 140자 사이여야 합니다"
                return render(request,'infoModify.html', context)

            user_instance = User.objects.get(username=userid)
            profile_instance = Profile.objects.get(username=userid)

            src = p.image
            if profilepic:
                i = Image(image=profilepic)
                i.save()
                img = Image.objects.last()
                src = 'img/' + str(img.image)
                profile_instance.image = src
                profile_instance.save()

            if password == "":
                user_instance.username = userid
                user_instance.email = email
                user_instance.first_name = name
                user_instance.save()
                context = {'user': request.user, 'ProfilePic': src, 'error': ""}
            else:
                user_instance.username = userid
                user_instance.email = email
                user_instance.first_name = name
                user_instance.password = make_password(password)
                user_instance.save()
                context = {'user': request.user, 'ProfilePic': src, 'error': ""}
        return render(request,'infoModify.html', context)
    return render(request,'login.html',context)

def decDetail(request):
    return render(request,'decDetail.html')

def ajaxupload(request):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        #캔버스로부터 가져온 이미지 저장
        image = request.POST.get('image', None)
        content = request.POST.get('content', None)
        src = request.POST.get('src', None)
        owner = request.user.username
        if image != "":
            image = image[22:]
            img = open('frivacyApp'+src, "wb")
            img.write(base64.b64decode(image))
            img.close()
        p = Post(owner=owner, image=src[8:], content=content)
        p.save()
        #포스트 리스트 불러오기
        out = []
        followerslist = [request.user.username]
        profilepics = {}

        for follower in Follower.objects.filter(follower=request.user.username):
            followerslist.append(follower.user)

        for user in Profile.objects.filter(username__in=followerslist):
            profilepics[user.username] = user.image
            if user.image == "":
                profilepics[user.username] = "img/default.png"
        for item in Post.objects.filter(owner__in=followerslist).order_by('-date_uploaded'):
            out.append(
                {"PostID": item.id, "URL": item.image, "Content": item.content, "Owner": item.owner,
                 "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                 "ProfilePic": profilepics[item.owner]})
        context = {'user': request.user, 'ProfilePic': p.image, 'posts':out}
        return render(request,'home.html', context)

    return render(request,'login.html',context)
    
def detail(request, noticeid):
    context = {}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        if request.method == 'GET': #공지사항 가져오기
            out = []
            item = Notice.objects.filter(id=noticeid)[0]
            out.append({"NoticeID": item.id, "Content": item.content, "Owner": item.owner,
                    "DateUploaded": item.date_uploaded.strftime("%Y-%m-%d %H:%M:%S"),
                    "Title": item.title})
            context = {'user': request.user, 'ProfilePic': p.image, 'posts':out}
        return render(request,'detail.html',context)
    return render(request,'login.html',context)
    
def new(request):
    return render(request,'new.html')

def notDetail(request):
    return render(request,'notDetail.html')

def followact(request, userid):
    context={}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        if request.method == 'GET':
            f = Follower(user=userid, follower=request.user)
            f.save()
        return render(request,'home.html', context)
    return render(request,'login.html', context)

def unfAct(request, userid):
    context={}
    if request.user.is_authenticated:
        p = Profile.objects.filter(username=request.user)[0]
        if p.image == "":
            p.image = "img/default.png"
        if request.method == 'GET':
            Follower.objects.get(user=userid, follower=request.user).delete()
        return render(request,'home.html', context)
    return render(request,'login.html', context)


