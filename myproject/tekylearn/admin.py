from re import I
from django.contrib import admin
from .models import learn_online,learn_title,learn_teacher_number,learn_intro,start_learn,learn_forcing,img_forcing,learn_prize,learn_why,learn_parent

# Register your models here.
class LearnWhy(admin.ModelAdmin):
    list_display = ['title','content']
    list_filter = ['title']
    search_fields =['title']
admin.site.register(learn_why, LearnWhy)


class LearnOnlineAdmin(admin.ModelAdmin):
    list_display = ['title','grade','subject']
    list_filter = ['grade']
    search_fields =['title']
admin.site.register(learn_online, LearnOnlineAdmin)


class LearnTitleAdmin(admin.ModelAdmin):
    list_display = ['name','title_small','title_big']
    list_filter = ['name']
    search_fields =['name']
admin.site.register(learn_title, LearnTitleAdmin)

class Teacher_numberAdmin(admin.ModelAdmin):
    list_display = ['name','number']
    list_filter = ['name']
    search_fields =['name']
admin.site.register(learn_teacher_number, Teacher_numberAdmin)

class LearnIntroAdmin(admin.ModelAdmin):
    list_display = ['title','content']
    list_filter = ['title']
    search_fields =['title']
admin.site.register(learn_intro, LearnIntroAdmin)


class Start_learnAdmin(admin.ModelAdmin):
    list_display = ['title','content']
    list_filter = ['title']
    search_fields =['title']
admin.site.register(start_learn, Start_learnAdmin)

class Img_Forcing_Admin(admin.TabularInline):
    model = img_forcing

class Learn_Forcing_Admin(admin.ModelAdmin):
    list_display = ['pos','name']
    list_filter = ['name']
    search_fields =['name']
    inlines = [Img_Forcing_Admin]
admin.site.register(learn_forcing, Learn_Forcing_Admin)

class img(admin.ModelAdmin):
    list_display = ['name','img']
admin.site.register(img_forcing, img)


class learn_prize_admin(admin.ModelAdmin):
    list_display = ['title','name']
admin.site.register(learn_prize, learn_prize_admin)


class LearnParent(admin.ModelAdmin):
    list_display = ['name','content']
    list_filter = ['name']
    search_fields =['name']
admin.site.register(learn_parent, LearnParent)