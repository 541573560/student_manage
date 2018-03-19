from django.contrib import admin
from .models import gratudated_and_employ,update_massage,parents,student_personal_massage

admin.site.register(student_personal_massage)
admin.site.register(parents)
admin.site.register(gratudated_and_employ)
admin.site.register(update_massage)