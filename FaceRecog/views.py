from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def capture(request):
    return render(request, 'capture.html')

def show(request):
    return render(request, 'show.html')

def start(request):
    return render(request, 'start.html')

def reg_teacher(request):
    return render(request, 'reg_teacher.html')

def reg_student(request):
    return render(request, 'reg_student.html')