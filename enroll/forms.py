from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Employee


class SignUPForm(UserCreationForm):
    password1= forms.CharField(label="Password" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
    class Meta:
        model = User
        fields = ["username", "first_name","last_name" , "email"]
        labels = {"email" : "Email", "first_name":"First Name" , "last_name" : "Last Name"}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ["username"]



class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["empId","empName","email","department","joindate"]
        labels = {"empId":"Employee Id","empName":"Name", "email":"Email :","department":"Department" , "joindate" : "Joining Date"}
        widgets = {
            "empId":forms.TextInput(attrs={'class':"form-control"}),
            "empName":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "department":forms.TextInput(attrs={'class':'form-control'}),
            "joindate":forms.DateInput(attrs={'class':'form-control'}),
            
            }
