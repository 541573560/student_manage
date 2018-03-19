from django.shortcuts import render
from django.http import HttpResponse
#自定义类
from .forms import Add_personal_massage

def index(request):
    if request.method == 'POST':

        form = Add_personal_massage(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse(form)#返回显示信息的主页

    else:
        form = Add_personal_massage()
        return render(request,'student/personal_massage.html',{'form':form})
