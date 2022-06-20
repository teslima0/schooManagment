import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from .models import Courses, CustomUser, SessionYearModel
from .forms import SessionForm
from django.shortcuts import render, redirect, HttpResponse
from tutorial.EmailBackEnd import EmailBackEnd
from django.contrib import auth

def showDemoPage(request):
    return render(request,"demo.html")

def Signup_admin(request):
    return render(request,"hod_template/signup_admin.html")
    

def do_staff_signup(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    address=request.POST.get('address')
    
    try:
        user= CustomUser.objects.create_user(username=username,password=password,email=email, user_type=2)
        user.staffs.address=address
        user.save()
        messages.success(request,"Staff account  created successfully ")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"fail to create Staff")
        return HttpResponseRedirect(reverse("show_login"))

def do_admin_signup(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    
    try:
        user= CustomUser.objects.create_user(username=username,password=password,email=email, user_type=1)
        user.save()
        messages.success(request,"Admin  created successfully ")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"fail to create admin")
        return HttpResponseRedirect(reverse("show_login"))

def Signup_student(request):
    courses=Courses.objects.all()
    session_years=SessionYearModel.object.all()
    return render(request,"student_template/signup_student.html",{"courses":courses, 'session_years':session_years})

def do_student_signup(request):
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")
    session_year_id=request.POST.get("session_year")
           
    course_id=request.POST.get("course")
    sex=request.POST.get("sex")

    profile_pic=request.FILES['profile_pic']
    fs=FileSystemStorage()
    filename=fs.save(profile_pic.name,profile_pic)
    profile_pic_url=fs.url(filename)

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
        user.students.address=address
        course_obj=Courses.objects.get(id=course_id)
        user.students.course_id=course_obj
                            
        session_year=SessionYearModel.object.get(id=session_year_id)
        user.students.session_year_id=session_year
                                
        user.students.gender=sex
        user.students.profile_pic=profile_pic_url
        user.save()
        messages.success(request,"Successfully Added Student")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Add Student")
        return HttpResponseRedirect(reverse("show_login"))
   

def Signup_staff(request):
    return render(request,"staff_template/signup_staff.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=authenticate(request, username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("show_login")

def logout_users(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from websites..')
        return redirect('show_login')

def logout_view(request):
    logout(request)
    return redirect('show_login')