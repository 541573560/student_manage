from django.shortcuts import render
from django.http import HttpResponse

#个人信息提交响应函数
def index(request):
    from .forms import Add_personal_massage
    if request.method == 'POST':
        form = Add_personal_massage(request.POST)
        if form.is_valid():
            massage = form.save(commit=False)
            massage.student_id = request.user
            massage.save()
            return HttpResponse('success')#返回显示信息的主页

    else:
        form = Add_personal_massage(
            # initial=[{'student_id':request.user},]
        )
        return render(request,'student/personal_massage.html',{'form':form})

#学生个人信息 查看 页面响应函数
def student_massage_page(request):
    from .models import student_personal_massage
    students = student_personal_massage.objects.filter(student_id=request.user)
    return render(request,'student/parsonal_passage_show.html',{'students':students})

#家庭信息 查看 页面响应函数
def parents_page(request):
    from .models import parents
    parent = parents.objects.filter(stu_id=request.user)
    return render(request,'student/parents_page_show.html',{'parent':parent})

#家庭信息 提交 页面响应函数
def parents_page_commit(request):
    from .forms import parents_massage
    if request.method == 'POST':
        form = parents_massage(request.POST)
        if form.is_valid():
            #增加数据
            massage = form.save(commit=False)
            massage.stu_id = request.user
            massage.save()
            return HttpResponse('ok')

    else:
        form = parents_massage()
        return render(request,'student/parents_massage_add.html',{'form':form})

#变更信息 显示 响应函数
def update_page(request):
    from .models import update_massage
    mysels = update_massage.objects.filter(stu_id=request.user)
    return render(request,'student/update_show.html',{'mysels':mysels})

#变更信息 提交 响应函数
def update_page_add(request):
    from .forms import Update_massage
    if request.method == 'POST':
        update = Update_massage(request.POST)
        if update.is_valid():
            #增加数据
            update.save()
            return HttpResponse('ok')

    else:
        update = Update_massage()
        return render(request,'student/update_add.html',{'update':update})

#毕业就业信息 显示 响应函数
def gratuate_page(request):
    from .models import gratudated_and_employ
    condition = request.user
    gratuated = gratudated_and_employ.objects.filter(stu_id=condition)
    return render(request,'student/gratuated_show.html',{'gratuated':gratuated})

#毕业就业信息 提交 响应函数
def gratuate_page_add(request):
    from .forms import Gratuations
    if request.method == 'POST':
        gratuated = Gratuations(request.POST)
        if gratuated.is_valid():
            #增加数据
            gratuated.save()
            return HttpResponse('ojbk')

    else:
        gratuated = Gratuations()
        return render(request,'student/gratuated_add.html',{'gratuated':gratuated})