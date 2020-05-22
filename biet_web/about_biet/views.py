from django.shortcuts import render
from .models import Academic_Calender

# Create your views here.
def Bapuji_educational_association(request):
    return render(request,'about_biet/Bapuji_educational_association.html')

def Vision_Mission_Quality_Policies(request):
    return render(request,'about_biet/bietHome.html')

def academic_calender(request):
    academic_calender = Academic_Calender.objects.all()
    return render(request,'about_biet/academic_calender.html',{'academic_calender' : academic_calender})

def governing_body(request):
    return render(request,'about_biet/governing_body.html')

def major_events(request):
    return render(request,'about_biet/major_events.html')

def nba(request):
    return render(request,'about_biet/nba.html')

def nain(request):
    return render(request,'about_biet/nain.html')

def naac(request):
    return render(request,'about_biet/naac.html')

def nirf(request):
    return render(request,'about_biet/nirf.html')
