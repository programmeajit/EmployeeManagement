from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUPForm,LoginForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
import qrcode
from datetime import date
from .forms import EmployeeFrom
from .models import Employee
from django.views import View
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.
# Home
class home(View):
    def post(self,request):
    
        fm = EmployeeFrom(request.POST)
        if fm.is_valid():
            fm.save()
            empDetails = Employee.objects.all()
            form = fm
            fm = EmployeeFrom()
            return render(request,"enroll/home.html",{"form":form, "empDetails":empDetails})
            
    def get(self,request):
        fm = EmployeeFrom()
        empDetails = Employee.objects.all()
    
        return render(request,"enroll/home.html",{"form":fm, "empDetails":empDetails})
# signup
def user_signup(request):
    if request.method == "POST":
        fm = SignUPForm(request.POST)
        if fm.is_valid():
            user = fm.save()
    else:
        fm = SignUPForm()
    return render(request, 'enroll/signup.html' ,{"form" : fm})


# Logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data =request.POST)
            if fm.is_valid():
                uname  = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            fm = LoginForm()
        return render(request, 'enroll/login.html',{"form":fm})
    else:
        return HttpResponseRedirect('/')

class update_data(View):
    def get(self,request,my_id):
        pi = Employee.objects.get(pk=my_id)
        fm = EmployeeFrom(instance=pi)
        return render(request, "enroll/update.html", {"form":fm})
    def post(self,request,my_id):
        pi = Employee.objects.get(pk=my_id)
        fm = EmployeeFrom(request.POST, instance=pi)
        print(pi)
        if fm.is_valid():
            fm.save()
        return render(request, "enroll/update.html", {"form":fm})
   
class delete_data(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['my_id']
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return super().get_redirect_url(*args,**kwargs)
 
