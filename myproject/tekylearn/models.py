from ast import mod
from distutils.command.upload import upload
from ntpath import join
from turtle import ondrag
from wsgiref import validate
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class learn_why(models.Model):
    title = models.CharField(max_length = 100, blank=False, null= False)
    content = models.TextField(blank=False, null= False)
    img = models.ImageField(upload_to = 'tekylearn/static/images/upload')
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.title
class learn_online(models.Model):
    title = models.CharField(max_length = 100, blank=False, null= False)
    grade = models.CharField(max_length = 10, blank=False, null= False)
    subject = models.CharField(max_length = 50, blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.title

class learn_title(models.Model):
    name =  models.CharField(max_length = 100, blank=False, null= False)
    title_small = models.CharField(max_length = 100, blank=False, null= False)
    title_big =  models.CharField(max_length = 100, blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name
class learn_teacher_number(models.Model):
    name =   models.CharField(max_length = 100, blank=False, null= False)
    number = models.IntegerField( blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name
class learn_intro(models.Model):
    title =   models.CharField(max_length = 100, blank=False, null= False)
    content = models.TextField( blank=False, null= False)
    img = models.FileField(upload_to='tekylearn/static/images/upload', validators =[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.title


class start_learn(models.Model):
    title =   models.CharField(max_length = 100, blank=False, null= False)
    content = models.TextField( blank=False, null= False)
    number = models.IntegerField( blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.title

class learn_forcing(models.Model):
    pos =   models.CharField(max_length = 100, blank=False, null= False)
    name = models.CharField(max_length = 100, blank=False, null= False)
    intro = models.TextField( blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name 
    @property
    def getimg(self):
        img = img_forcing.objects.filter(name = self.id, typeimg = "normal")
        return img
    @property
    def getimgmain(self):
        img = img_forcing.objects.filter(name = self.id,typeimg = "main")
        return img

class img_forcing(models.Model):
    name = models.ForeignKey(learn_forcing, on_delete=models.CASCADE, related_name='test')
    img = models.ImageField(upload_to='tekylearn/static/images/upload')
    typeimg = models.CharField(max_length = 10, blank=False, null= False, default="normal")
    def __str__(self):
        return self.name.name   
    
class learn_prize(models.Model):
    title = models.CharField(max_length = 100, blank=False, null= False)
    name = models.CharField(max_length = 100, blank=False, null= False)
    img = models.ImageField(upload_to = 'tekylearn/static/images/upload')
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.title

class learn_parent(models.Model):
    name = models.CharField(max_length = 100, blank=False, null= False)
    poi = models.CharField(max_length = 100, blank=False, null= False)
    content = models.TextField(blank=False, null= False)
    img = models.ImageField(upload_to = 'tekylearn/static/images/upload')
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name

class customer(models.Model):
    username = models.CharField(max_length = 100, blank=False, null= False)
    password = models.CharField(max_length = 100, blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)

class trungtam(models.Model):
    name = models.CharField(max_length = 100, blank=False, null= False)
    address = models.CharField(max_length = 100, blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    
    def __str__(self):
        string = self.address+ " - "+self.name
        return string

class CapHoc(models.Model):
    name = models.CharField(max_length = 100, blank=False, null= False)
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name

class RegisterStudent(models.Model):
    name = models.CharField(max_length = 100, blank=False, null= False)
    phone  = models.CharField(max_length = 11, blank=False, null= False)
    caphoc = models.ForeignKey(CapHoc,  on_delete=models.CASCADE, related_name='test')
    trungtam = models.ForeignKey(trungtam,  on_delete=models.CASCADE, related_name='test')
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length = 100, blank=False, null= False)
    img = models.ImageField(upload_to = 'tekylearn/static/images/upload')
    location = models.IntegerField(blank=False, null= False, default=0)
    def __str__(self):
        return self.name


class blog1(models.Model):
    title = models.CharField(max_length = 100, blank=False, null= False)
    content =models.TextField(blank=False, null= False)
    number = models.CharField(max_length = 10, blank=False, null= False)
    img = models.ImageField(upload_to = 'tekylearn/static/images/upload')
    def __str__(self):
        return self.title