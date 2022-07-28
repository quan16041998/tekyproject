from ast import Expression, Try
from dataclasses import field
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import customer,RegisterStudent,trungtam,CapHoc

class TestForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('username', 'password')
        widgets = {
            'username' : forms.TextInput(attrs= {'class' : 'form-control c-placeholder-login'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control c-placeholder-login'})
        }  
    def clean_username(self):
        username = self.cleaned_data['username'] 
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("The username you entered is incorrect")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterStudent
        fields = {'name','phone','caphoc','trungtam'}
        widgets = {
            'name' : forms.TextInput(attrs= {'class' : 'form-control c-placeholder-login'}),
            'phone' : forms.TextInput(attrs= {'class' : 'form-control c-placeholder-login'}),
            'caphoc' : forms.Select(choices= CapHoc.objects.order_by('location').values_list('name'), attrs={'class' : 'form-control c-placeholder-login'}),
            'trungtam' : forms.Select(choices= trungtam.objects.all().order_by('-location'), attrs={'class' : 'form-control c-placeholder-login'})
        }


class RegisterUserForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30, widget=forms.TextInput(attrs= {'class' : 'form-control c-placeholder-login'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs= {'class' : 'form-control c-placeholder-login'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs= {'class' : 'form-control c-placeholder-login'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs= {'class' : 'form-control c-placeholder-login'}))
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password1
        raise forms.ValidationError("The entered passwords do not match.Try again") 
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("The username you entered is incorrect")   
    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'],email = self.cleaned_data['email'],password = self.cleaned_data['password1'])