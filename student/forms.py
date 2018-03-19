from django import forms
from student.models import student_personal_massage,parents,gratudated_and_employ,update_massage

#表单1，学生基本信息表单，内置反法为直接将信息存储至数据库
class Add_personal_massage(forms.Form):
    student_id = forms.CharField(max_length=30,label="学号")
    name = forms.CharField(max_length=10,label="姓名")
    sex = forms.CharField(max_length=10,label="性别")
    family_address = forms.CharField(max_length=50,label="家庭住址")
    acdemy = forms.CharField( max_length=15,label="所属学院")
    class_num = forms.CharField(max_length=15,label="班级")
    train_level = forms.CharField(max_length=5,label="学制")
    registered_residence = forms.CharField(max_length=20,label="入学前户口")
    length_of_schooling = forms.CharField(max_length=10,label="学制")
    Political_level = forms.CharField(max_length=20,label="政治面貌")
    graduated_high_school = forms.CharField(max_length=20,label="高中毕业学校")
    graduation_grades = forms.IntegerField(label="高考总分")
    single_kinds = forms.CharField(max_length=5,label="是否独生子女")
    study_way = forms.CharField(max_length=15,label="入学前授课方式")

    def save(self):
        student_personal_massage.objects.create(
            student_id = self.student_id,
            name = self.name,
            sex=self.sex,
            family_address = self.family_address,
            acdemy = self.acdemy,
            class_num = self.class_num,
            train_level = self.train_level,
            registered_residence = self.registered_residence,
            length_of_schooling = self.length_of_schooling,
            Political_level = self.Political_level,
            graduated_high_school = self.graduated_high_school,
            graduation_grades = self.graduation_grades,
            single_kinds = self.single_kinds,
            study_way = self.study_way
        )

#表单2，父母信息类 定义save函数保存数据
class parents_massage(forms.Form):
    stu_id = forms.CharField(max_length=8)
    name = forms.CharField(max_length=10,label='姓名')
    birthday = forms.DateField(label='出生年月')
    relation_of_student = forms.CharField(max_length=6,label='与本人关系', help_text='父亲/母亲/妹妹')
    work_location = forms.CharField(max_length=20, label='工作单位')
    post = forms.CharField(max_length=10, label='职务')
    Political_level_p = forms.CharField(max_length=20, label='政治面貌')
    phone_number = forms.CharField(max_length=10, label='联系电话')
    healthy_condition = forms.CharField(max_length=10, label='健康状况')

    def save(self):
        parents.objects.create(
            stu_id = self.stu_id,
            name = self.name,
            birthday = self.birthday,
            relation_of_student = self.relation_of_student,
            work_location = self.work_location,
            post = self.post,
            Political_level_p = self.Political_level_p,
            phone_number = self.phone_number,
            healthy_condition = self.healthy_condition,
        )


class Update_massage():
    stu_id = forms.CharField(max_length=8)
    living_room = forms.CharField(max_length=6, label='所在宿舍')
    phone_number = forms.CharField(max_length=11, label='电话')
    pareants_single = forms.CharField(max_length=2, label='是/否单亲家庭')
    basic_living_allowances = forms.CharField(max_length=2, label='是否拥有最低城市/农村生活保障')
    orphan_disablity = forms.CharField(max_length=2, label='是/否孤残')
    martyr = forms.CharField(max_length=2, label='是/否烈士子女')
    party_member = forms.CharField(max_length=2, label='是/否党员')
    party_member_application = forms.CharField(max_length=2, label='是/否递交入党申请书')
    population = forms.CharField(max_length=5, label='家庭人口数')
    poor = forms.CharField(max_length=5, label='家庭是否困难', help_text='是/否')
    poor_reason = forms.CharField(max_length=50, label='困难原因')
    Instructor = forms.CharField(max_length=10, label='辅导员姓名')
    Instructor_nmber = forms.CharField(max_length=11, label='辅导员电话')

    def save(self):
        update_massage.objects.create(
            stu_id = self.stu_id,
            living_room = self.living_room,
            phone_number = self.phone_number,
            parents_single = self.pareants_single,
            basic_living_allowances = self.basic_living_allowances,
            orphan_disablity = self.orphan_disablity,
            martyr = self.martyr,
            party_menber = self.party_member,
            party_member_application = self.party_member_application,
            population = self.population,
            poor = self.poor,
            poor_reason = self.poor_reason,
            Instructor = self.Instructor,
            Instructor_nmber = self.Instructor_nmber
        )


class Gratuations():
    stu_id = forms.CharField(max_length=8)
    gratudated = forms.CharField(max_length=2, label='是否毕业')
    gratudated_reason = forms.CharField(max_length=200,label='未毕业原因', )
    degree = forms.CharField(max_length=2, label='是否授予学位',  help_text='可以不填，以下同上')
    degree_reason = forms.CharField(max_length=200,label='未授予学位原因')
    back_xinjiang = forms.CharField(max_length=2, label='是否返回新疆')
    employ_apartment = forms.CharField(max_length=15, label='就业单位')
    employ_apartment_manager = forms.CharField(max_length=5, label='就业单位联系人')
    employ_apartment_phone = forms.CharField(max_length=15, label='就业单位联系电话')

    def save(self):
        gratudated_and_employ.objects.create(
            stu_id=self.stu_id,
            gratudated = self.gratudated,
            gratudated_reason = self.gratudated_reason,
            degree = self.degree,
            degree_reason = self.degree_reason,
            back_xinjiang = self.back_xinjiang,
            employ_apartment = self.employ_apartment,
            employ_apartment_manager = self.employ_apartment_manager,
            employ_apartment_phone = self.employ_apartment_phone
        )


