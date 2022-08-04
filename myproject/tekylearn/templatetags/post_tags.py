
from django import template
from django.template.defaultfilters import stringfilter
from ..models import learn_forcing, learn_intro, learn_online, learn_teacher_number,learn_title, learn_why, start_learn

register = template.Library()

# @register.filter(is_save = True)
# @stringfilter
# def myfilter(value):
#     return value + " love you so much <3"


@register.filter()
def myfilter(value):
    return str(value) + "haha"

@register.simple_tag
def total_forcing():
    return learn_title.objects.count()

@register.inclusion_tag("blog1/learn-why.html")
def why(total):
    why = learn_why.objects.order_by("id")[:total]
    return {'why' :why}    

@register.inclusion_tag("blog1/learn-online.html")
def online(values, total):
    online = learn_online.objects.order_by(values)[:total]
    return {'online' : online}   

@register.inclusion_tag("blog1/learn-team.html")
def team(values, total):
    teacher = learn_teacher_number.objects.order_by(values)[:total]
    return {'teacher' : teacher}  

@register.inclusion_tag("blog1/learn-intro.html")
def intro(values, total):
    intro = learn_intro.objects.order_by(values)[:total]
    return {'intro' : intro} 

@register.inclusion_tag("blog1/learn-start.html")
def start(values, total):
    start = start_learn.objects.order_by(values)[:total]
    return {'start' : start} 

@register.inclusion_tag("blog1/learn-forcing.html")
def forcing(values, total):
    forcing = learn_forcing.objects.order_by(values)[:total]
    return {'forcing' : forcing} 

@register.simple_tag
def alltitle():
    title = learn_title.objects.all()
    return title

@register.simple_tag
def learn_forcing_img(id):
    forcing = learn_forcing.objects.get(id = id)
    img = forcing.getimg
    return img

@register.simple_tag
def learn_forcing_imgmain(id):
    forcing = learn_forcing.objects.get(id = id)
    img = forcing.getimgmain
    return img