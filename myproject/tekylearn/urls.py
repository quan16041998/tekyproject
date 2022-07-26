
from django.urls import path, include
from . import views
urlpatterns = [
    path('tekylearn/', views.teky_learn.as_view())
]