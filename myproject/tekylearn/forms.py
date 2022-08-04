from ast import Expression, Try
from dataclasses import field
from email.policy import default

from unittest.util import _MAX_LENGTH
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import ModalRegisterStudent, customer,RegisterStudent

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
        YEAR_CHOICES = [
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
        (2020, '2020'),
        ]
        model = ModalRegisterStudent
        fields = {'name','year','nameparent','email','phonenumber'}
        widgets = {
            'name' : forms.TextInput(attrs= {'class' : 'form-control','placeholder' : 'Nhập họ và tên học sinh'}),
            'year' : forms.Select(choices= YEAR_CHOICES,attrs={'class':'form-control'}),
            'nameparent' : forms.TextInput(attrs= {'class' : 'form-control','placeholder': 'Nhập họ và tên phụ huynh'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control','placeholder' : 'Nhập email liên hệ'}),
            'phonenumber' : forms.TextInput(attrs= {'class' : 'form-control','placeholder' : 'Nhập số điện thoại liên hệ'})
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
    def clean_email1(self):
        email = self.cleaned_data['email']
        if User.objects.get(email = email) :
            raise forms.ValidationError("The email you entered is incorrect")   
        else:
            return email
    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'],email = self.cleaned_data['email'],password = self.cleaned_data['password1'])