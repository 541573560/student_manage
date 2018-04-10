from django.shortcuts import render

def page(request):
    from student.models import student_personal_massage
    if request.user == 'jisuanji':
        student = student_personal_massage.objects.filter(academy__contains='计算机')
        print('dwadwaad')
        return render(request, 'control/control.html', context={'stu_grouop': student})
    elif request.user == 'guojiao':
        pass
    elif request.user == 'jingjiguanli':
        pass
    elif request.user == 'jidian':
        pass
    elif request.user == 'cailiao':
        pass
    elif request.user == 'huaxuegongcheng':
        pass
    elif request.user == 'huaxueshengming':
        pass
    elif request.user == 'yishusheji':
        pass
    elif request.user == 'renwen':
        pass
    elif request.user == 'makesi':
        pass
    elif request.user == 'jichu':
        pass
    elif request.user == 'waiguoyu':
        pass
    elif request.user == 'yingyong':
        pass