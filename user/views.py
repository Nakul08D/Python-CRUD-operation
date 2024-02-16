from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import Student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def log(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return render(request,'login.html')

def login_info(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            return render(request,'login.html')

def signin(request):
    return render(request,'signin.html')

def signin_info(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password1=request.POST.get('password1')
        password2=request.POST.get('password1')

        st=User.objects.create_user(
            username=name,
            password=password1,
        )
        if password1!=password2:
            return render(request,'signin.html')
        else:
            st.save()
            return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def submit(request):
    if request.method=="POST":
        sno=request.POST.get('sno')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        language=request.POST.get('language')
        image=request.FILES.get('image')

        st=Student.objects.create(
            sno=sno,
            fname=fname,
            lname=lname,
            language=language,
            image=image
            )
        st.save()
    #return redirect('/')
    return render(request,'home.html')

def s_list(request):
    st=Student.objects.all()
    context={'st':st}
    return render(request,'s_list.html',context)

def edit(request,id):
    st=Student.objects.get(id=id)
    context={'st':st}
    return render(request,'edit.html',context)

def update(request,id):
    if request.method=='POST':
        sno=request.POST.get('sno')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        language=request.POST.get('language')

        st=Student.objects.get(id=id)
        
        if request.FILES.get('image') is  None: 
            st.image = st.image
        else:
            img=request.FILES.get('image')
            st.image=img
    
        st.sno=sno
        st.fname=fname
        st.lname=lname
        st.language=language

        st.save()
        #return redirect('/')
        return render(request,'home.html')


def delete(request,id):
    st=Student.objects.get(id=id)
    st.delete()
    st=Student.objects.all()
    return render(request,'s_list.html',{'st':st})
