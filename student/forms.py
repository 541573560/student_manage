from django import forms

#表单1，学生基本信息表单，内置反法为直接将信息存储至数据库
class Add_personal_massage(forms.Form):
    student_id = forms.CharField(
        max_length=30,
        label="学号"
    )
    name = forms.CharField(
        max_length=10,
        label="姓名"
    )
    sex = forms.CharField(
        max_length=10,
        label="性别"
    )
    family_address = forms.CharField(
        max_length=50,
        label="家庭住址"
    )
    acdemy = forms.CharField(
        max_length=15,
        label="所属学院"
    )
    class_num = forms.CharField(
        max_length=15,
        label="班级"
    )
    train_level = forms.CharField(
        max_length=5,
        label="学制"
    )
    registered_residence = forms.CharField(
        max_length=20,
        label="入学前户口"
    )
    length_of_schooling = forms.CharField(
        max_length=10,
        label="学制"
    )
    Political_level = forms.CharField(
        max_length=20,
        label="政治面貌"
    )
    graduated_high_school = forms.CharField(
        max_length=20,
        label="高中毕业学校"
    )
    graduation_grades = forms.IntegerField(
        label="高考总分"
    )
    single_kinds = forms.CharField(
        max_length=5,
        label="是否独生子女"
    )
    study_way = forms.CharField(
        max_length=15,
        label="入学前授课方式"
    )

    def save(self):
        #存储表单数据方法，调用固定的sql orm
        pass


class parents(forms.Form):
    pass