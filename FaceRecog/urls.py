from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from FaceRecog import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('about', views.about, name = 'about'),
    path('capture', views.capture, name = 'capture'),
    path('show', views.show, name = 'show'),
    path('start', views.start, name = 'start'),
     path('reg_teacher', views.reg_teacher, name = 'reg_teacher'),
      path('reg_student', views.reg_student, name = 'reg_student')

]

