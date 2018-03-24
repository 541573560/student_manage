from django.forms import ModelForm
from student import models

#form.py文件定义了四个表单，用于用户提交信息。
#表单1，学生基本信息表单，内置反法为直接将信息存储至数据库
class Add_personal_massage(ModelForm):
    class Meta:
        model = models.student_personal_massage
        fields = "__all__"

#表单2，父母信息类
class parents_massage(ModelForm):
    class Meta:
        model = models.parents
        fields = "__all__"


#表单3，变更信息类
class Update_massage(ModelForm):
    class Meta:
        model = models.update_massage
        fields = "__all__"



#毕业就业类
class Gratuations(ModelForm):
    class Meta:
        model = models.gratudated_and_employ
        fields = "__all__"



