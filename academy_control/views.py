from django.shortcuts import render
from django.shortcuts import HttpResponse

def check_stu_massage(request):
    from student.models import student_personal_massage
    user_name = str(request.user)
    if user_name == 'jisuanji':
        student = student_personal_massage.objects.filter(academy__contains='计算机')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'guojiao':
        pass
    elif user_name == 'jingjiguanli':
        pass
    elif user_name == 'jidian':
        pass
    elif user_name == 'cailiao':
        pass
    elif user_name == 'huaxuegongcheng':
        pass
    elif user_name == 'huaxueshengming':
        pass
    elif user_name == 'yishusheji':
        pass
    elif user_name == 'renwen':
        pass
    elif user_name == 'makesi':
        pass
    elif user_name == 'jichu':
        pass
    elif user_name == 'waiguoyu':
        pass
    elif user_name == 'yingyong':
        pass
    else:
        return HttpResponse('您尚未登录')

def detil_massage():
    pass