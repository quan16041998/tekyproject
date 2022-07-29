
from django.contrib import messages 
from unicodedata import name
from django import forms
from django.shortcuts import redirect, render
from django.views import View
from .serializers import UserSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, RegisterUserForm, TestForm
from .models import Partner, learn_intro,learn_online,learn_parent,learn_teacher_number, learn_title, learn_why, start_learn,learn_forcing,learn_prize,blog1
# Create your views here.


class teky_learn(LoginRequiredMixin, View):
    login_url = 'login/'
    def get(self, request):
        blog = blog1.objects.get(id=1)
        why = learn_why.objects.all()
        online = learn_online.objects.all()
        teacher = learn_teacher_number.objects.all()
        intro = learn_intro.objects.all()
        start = start_learn.objects.all()
        forcing = learn_forcing.objects.all()
        title_learn =  learn_title.objects.all()
        prize = learn_prize.objects.all()
        parent = learn_parent.objects.all()
        partner = Partner.objects.all()
        context = { 'why': why, 'online' : online ,'teacher' : teacher, 'intro' : intro,'blog' :blog,
        'start' :start, 'forcing': forcing,'title' : title_learn,'prize':prize,'parent':parent,'partner' : partner
        }
        return render(request, 'teky-learn.html',context)

class loginClass(View):
    def get(self,request):
        form = TestForm()
        return render(request,'login.html',{'form' : form})

    def post(self,request):
        user_name = request.POST['username']
        pass_word = request.POST['password']
        request.session['username'] =  user_name
        f = TestForm(request.POST)
        user = authenticate(request,username= user_name,password = pass_word)   
        if user is None:
            messages.error(request,'Username or Password is incorrect')
            return redirect('login')
        else:
            login(request, user)
            return redirect('tekylearn')

def logoutview(request):
    logout(request)
    return redirect('login')

class RegisterClass(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'register.html', {'form' : form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tekylearn')
        else:
            return HttpResponse('Fall')

class RegisterUserClass(View):
    def get(self,request):
        form = RegisterUserForm()
        return render(request,'registeruser.html',{'form' :form})
    def post(self,request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully registered')
            return redirect('login')     
        return render(request, 'registeruser.html', {'form' :form})
        

def validate_username(request):
    if  request.method == "GET":
        username= request.GET.get("username", None)
        if User.objects.filter(username= username).exists():
            return JsonResponse({"valid":False}, status = 200)
        else:
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)


class ListUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new User successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
           