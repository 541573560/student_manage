from django.shortcuts import render
from django.http import HttpResponse
#自定义类
from .forms import Add_personal_massage,parents_massage,Update_massage,Gratuations
from .models import student_personal_massage,parents,update_massage,gratudated_and_employ

def index(request):
    if request.method == 'POST':

        form = Add_personal_massage(request.POST)

        if form.is_valid():
            #form.save()保存暂时没有
            return HttpResponse(form)#返回显示信息的主页
    else:
        form = Add_personal_massage()
        return render(request,'student/personal_massage.html',{'form':form})

def student_massage_page(request):
    student = student_personal_massage.objects.all()
    return render(request,'student/parsonal_passage_show.html',{'student':student})

def parents_page(request):
    pass

def parents_page_commit(request):
    if request.method == 'POST':
        pagrents = parents_massage(request.POST)
        if pagrents.is_valid():
            #增加数据
            return HttpResponse(pagrents)

    else:
        pagrents = parents_massage()
        return render(request,'student/parents_massage_add.html',{'pagrents':pagrents})


def update_page(request):
    pass

def update_page_add(request):
    if request.method == 'POST':
        update = Update_massage(request.POST)
        if update.is_valid():
            #增加数据
            return HttpResponse(update)

    else:
        update = Update_massage()
        return render(request,'student/update_add.html',{'update':update})

def gratuate_page(request):
    pass

def gratuate_page_add(request):
    if request.method == 'POST':
        gratuated = Gratuations(request.POST)
        if gratuated.is_valid():
            #增加数据
            return HttpResponse(gratuated)

    else:
        gratuated = Gratuations()
        return render(request,'student/gratuated_add.html',{'gratuated':gratuated})