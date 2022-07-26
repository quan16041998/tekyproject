from django.shortcuts import render
from django.views import View
from urllib import request
from django.http import HttpResponse
from .models import learn_intro,learn_online,learn_parent,learn_teacher_number, learn_title, learn_why, start_learn,learn_forcing,learn_prize
# Create your views here.


class teky_learn(View):
    def get(self, request):
        why = learn_why.objects.all()
        online = learn_online.objects.all()
        teacher = learn_teacher_number.objects.all()
        intro = learn_intro.objects.all()
        start = start_learn.objects.all()
        forcing = learn_forcing.objects.all()
        title_learn =  learn_title.objects.all()
        prize = learn_prize.objects.all()
        parent = learn_parent.objects.all()
        number = [1,2,3,4,5,6]
        return render(request, 'teky-learn.html',{ 'why': why, 'online' : online ,'teacher' : teacher, 'intro' : intro, 
        'start' :start, 'forcing': forcing,'title' : title_learn,'number' : number, 'prize':prize,'parent':parent
        })
