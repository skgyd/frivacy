from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

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

