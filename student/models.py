from django.db import models

class student_personal_massage(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=10, verbose_name='姓名')
    sex = models.CharField(max_length=10, blank=True, verbose_name='性别')
    family_address = models.CharField(max_length=50,default=None, blank=True, verbose_name='家庭住址')
    academy = models.CharField(max_length=15,default=None, blank=True, verbose_name='学院')
    class_num = models.CharField(max_length=100, blank=True, verbose_name='班级')
    train_level = models.CharField(max_length=5,blank=True,verbose_name='学制',help_text='本科/专科')
    registered_residence = models.CharField(max_length=20, verbose_name='入学前户口')
    length_of_schooling = models.CharField(max_length=10, verbose_name='学制', help_text='例如四年/三年')
    Political_level = models.CharField(max_length=20, verbose_name='政治面貌')
    graduated_high_school = models.CharField(max_length=20, verbose_name='高中毕业学校')
    graduation_grades = models.IntegerField(verbose_name='高考总分')
    single_kinds = models.CharField(max_length=5, verbose_name='是否独生子女')
    study_way = models.CharField(max_length=15, verbose_name='入学前授课方式', help_text='汉语/其他语言')

    #class Meta:
    #    verbose_name = '学生基本信息'
    #    verbose_name_plural = '学生基本信息填写'

    def __str__(self):
        return self.student_id

class parents(models.Model):
    stu_id = models.CharField(max_length=8)
    name = models.CharField(max_length=10, verbose_name='姓名')
    birthday = models.DateField(verbose_name='出生年月')
    relation_of_student = models.CharField(max_length=6, verbose_name='与本人关系', help_text='父亲/母亲/妹妹')
    work_location = models.CharField(max_length=20, verbose_name='工作单位')
    post = models.CharField(max_length=10, verbose_name='职务')
    Political_level_p = models.CharField(max_length=20, verbose_name='政治面貌')
    phone_number = models.CharField(max_length=10, verbose_name='联系电话')
    healthy_condition = models.CharField(max_length=10, verbose_name='健康状况')

    def __str__(self):
        return self.name


    #class Meta:
    #    verbose_name = '家庭信息'
    #    verbose_name_plural = '家庭信息'

class update_massage(models.Model):
    stu_id = models.CharField(max_length=8)
    date = models.DateField(auto_now_add=True,auto_created=True)
    living_room = models.CharField(max_length=6,verbose_name='所在宿舍')
    phone_number = models.CharField(max_length=11,verbose_name='电话')
    pareants_single = models.CharField(max_length=2,verbose_name='是/否单亲家庭')
    basic_living_allowances = models.CharField(max_length=2,verbose_name='是否拥有最低城市/农村生活保障')
    orphan_disablity = models.CharField(max_length=2,verbose_name='是/否孤残')
    martyr = models.CharField(max_length=2,verbose_name='是/否烈士子女')
    party_member = models.CharField(max_length=2,verbose_name='是/否党员')
    party_member_application = models.CharField(max_length=2,verbose_name='是/否递交入党申请书')
    population = models.CharField(max_length=5,verbose_name='家庭人口数')
    poor = models.CharField(max_length=5,verbose_name='家庭是否困难',help_text='是/否')
    poor_reason = models.CharField(max_length=50,blank=True,verbose_name='困难原因')
    Instructor = models.CharField(max_length=10,verbose_name='辅导员姓名')
    Instructor_nmber = models.CharField(max_length=11,verbose_name='辅导员电话')

    def __str__(self):
        return self.id


    #class Meta:
    #    verbose_name = '就读信息'
    #    verbose_name_plural = '就读信息'

class gratudated_and_employ(models.Model):
    stu_id = models.CharField(max_length=8)
    date = models.DateField(auto_now_add=True,auto_created=True)
    gratudated = models.CharField(max_length=2,verbose_name='是否毕业')
    gratudated_reason = models.CharField(max_length=200,verbose_name='未毕业原因',default=None,blank=True)
    degree = models.CharField(max_length=2,verbose_name='是否授予学位',default=None,blank=True,help_text='可以不填，以下同上')
    degree_reason = models.CharField(max_length=200,verbose_name='未授予学位原因',default=None,blank=True)
    back_xinjiang = models.CharField(max_length=2,verbose_name='是否返回新疆')
    employ_apartment = models.CharField(max_length=15,verbose_name='就业单位',default=None,blank=True)
    employ_apartment_manager = models.CharField(max_length=5,verbose_name='就业单位联系人',default=None,blank=True)
    employ_apartment_phone = models.CharField(max_length=15,verbose_name='就业单位联系电话',default=None,blank=True)

    def __str__(self):
        return self.employ_apartment

    class Meta:
        verbose_name_plural = '毕业就业'
        verbose_name = '毕业就业'