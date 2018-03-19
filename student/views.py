from django.shortcuts import render
from django.http import HttpResponse
#自定义类
from .forms import Add_personal_massage

def index(request):
    if request.method == 'POST':

        form = Add_personal_massage(request.POST)

        if form.is_valid():
            #在这里进入数据库
            return HttpResponse(form)

    else:
        form = Add_personal_massage()
        return render(request,'student/personal_massage.html',{'form':form})


