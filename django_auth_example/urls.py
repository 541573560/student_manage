"""django_auth_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from users import views
from student import views as s_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^student_massage_add/',s_views.index,name='index'),
    url(r'^student_massage_show/',s_views.student_massage_page,name='stu_page'),
    url(r'^parents_massage_add/',s_views.parents_page_commit,name='Pmas_add'),
    url(r'^update_add',s_views.update_page_add,name='up_add'),
    url(r'^gratuated_add',s_views.gratuate_page_add,name='gr_add'),
]
