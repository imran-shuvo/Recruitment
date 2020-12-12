from django.db import models
from django.db import models
import uuid


class File(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

class RecruitmentInfo(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=14)
    full_address = models.CharField(max_length=512)
    name_of_university = models.CharField(max_length=256)
    graduation_year = models.IntegerField(max=2020,min=2015)
    cgpa = models.IntegerField(max=4,min=2)
    experience_in_months = models.IntegerField(max=100,min=0)
    current_work_place_name = models.CharField(max_length=256)
    applying_in = models.CharField(max_length=14)
    expected_salary = models.IntegerField(max=60000,min=15000)
    field_buzz_reference = models.CharField(max_length=256)
    github_project_url = models.CharField(max_length=256)
    cv_file = models.ForeignKey(File,on_delete = None)
    on_spot_update_time = models.DateTimeField(auto_now=True)
    on_spot_creation_time = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.name




# Create your models here.
