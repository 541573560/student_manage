from django.shortcuts import render
from django.shortcuts import HttpResponse

def check_stu_massage(request):
    from student.models import student_personal_massage
    user_name = str(request.user)
    if user_name == 'jisuanji':
        student = student_personal_massage.objects.filter(academy__contains='计算机')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'guojiao':
        student = student_personal_massage.objects.filter(academy__contains='国际教育')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'jingjiguanli':
        student = student_personal_massage.objects.filter(academy__contains='经济管理')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'jidian':
        student = student_personal_massage.objects.filter(academy__contains='机电')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'cailiao':
        student = student_personal_massage.objects.filter(academy__contains='材料')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'huaxuegongcheng':
        student = student_personal_massage.objects.filter(academy__contains='化学工程')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'huaxueshengming':
        student = student_personal_massage.objects.filter(academy__contains='化学与生命')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'yishusheji':
        student = student_personal_massage.objects.filter(academy__contains='艺术')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'renwen':
        student = student_personal_massage.objects.filter(academy__contains='人文')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'makesi':
        student = student_personal_massage.objects.filter(academy__contains='马克思')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'jichu':
        student = student_personal_massage.objects.filter(academy__contains='基础')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'waiguoyu':
        student = student_personal_massage.objects.filter(academy__contains='外国语')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif user_name == 'yingyong':
        student = student_personal_massage.objects.filter(academy__contains='应用')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    else:
        return HttpResponse('您尚未登录')

def detil_massage(request,stu_id):
    from student.models import student_personal_massage,parents,update_massage,gratudated_and_employ
    student = student_personal_massage.objects.get(stu_id = stu_id)
    parent = parents.objects.filter(stu_id = stu_id)
    update = update_massage.objects.filter(stu_id = stu_id)
    gratuate = gratudated_and_employ.objects.filter(stu_id = stu_id)
    return render(request,'control/detil_mas.html',context={'student':student,'parent':parent,'update':update,'gratuate':gratuate})
