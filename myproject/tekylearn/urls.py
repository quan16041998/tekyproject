
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('tekylearn/', views.teky_learn.as_view(), name='tekylearn'),
    path('tekylearn/login/', views.loginClass.as_view(), name='login'),
    path('logout/',views.logoutview, name= 'logout'),
    path('register/', views.RegisterClass.as_view(), name='register'),
    path('registeruser/', views.RegisterUserClass.as_view(), name='registeruser'),
    path('validate_user/', views.validate_username, name='validate_username'),
    path('templatetags/', views.templatetags.as_view(), name="templatetagss"),
    path('auth/', include('social_django.urls', namespace='social'))
]