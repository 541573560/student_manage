from django.conf.urls import url

from academy_control import views

app_name = 'academy_control'

urlpatterns = [
    url(r'^massage/',views.check_stu_massage,name='control_stu_mas'),
    url(r'^detil/(\w+)/',views.detil_massage,name='show_detil'),
]