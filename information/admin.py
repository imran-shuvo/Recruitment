from django.contrib import admin

# Register your models here.
from .models import RecruitmentInfo,File
admin.site.register(RecruitmentInfo)
admin.site.register(File)

