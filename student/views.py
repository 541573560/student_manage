from django.shortcuts import render
from django.http import HttpResponse
#自定义类
from .forms import Add_personal_massage,parents_massage,Update_massage,Gratuations
from .models import student_personal_massage,parents,update_massage,gratudated_and_employ

def index(request):
    if request.method == 'POST':

        form = Add_personal_massage(request.POST)

        if form.is_valid():
            #form.save()
            return HttpResponse(form)#返回显示信息的主页
    else:
        form = Add_personal_massage()
        return render(request,'student/personal_massage.html',{'form':form})

def student_massage_page(request):
    student = student_personal_massage.objects.all()
    return render(request,'student/parsonal_passage_show.html',{'student':student})

def parents_page(request):
    pass

def update_page(request):
    pass

def gratuate_page(request):
    pass