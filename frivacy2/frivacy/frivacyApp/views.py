from django.shortcuts import render
from .forms import UploadDocumentForm, ImageForm
from .models import Image
from .detect_face_image import detecting
# Create your views here.

def home(request):
    form = UploadDocumentForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Image.objects.last()
            src = 'img/' + str(img.image)
            list = detecting(src).tolist()
            print(type(list))
            return render(request, 'home.html', {
                'list': list,
                'src': src
            })
    return render(request, 'home.html', locals())

def decEdit(request):
    return render(request,'decEdit.html')

def notice(request):
    return render(request,'notice.html')

def declaration(request):
    return render(request,'declaration.html')
    
def decNew(request):
    return render(request,'decNew.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
    
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
