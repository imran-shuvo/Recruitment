from django.db import models
from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class File(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

class RecruitmentInfo(models.Model):
    tsync_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=14)
    full_address = models.CharField(max_length=512)
    name_of_university = models.CharField(max_length=256)
    graduation_year = models.PositiveIntegerField(validators=[MinValueValidator(2015),MaxValueValidator(2020)])
    cgpa = models.PositiveIntegerField(validators=[MinValueValidator(2),MaxValueValidator(4)])
    experience_in_months = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    current_work_place_name = models.CharField(max_length=256)
    applying_in = models.CharField(max_length=14)
    expected_salary = models.PositiveIntegerField(validators=[MinValueValidator(15000),MaxValueValidator(60000)])
    field_buzz_reference = models.CharField(max_length=256)
    github_project_url = models.CharField(max_length=256)
    cv_file = models.ForeignKey(File,on_delete = callable)
    on_spot_update_time = models.DateTimeField(auto_now=True)
    on_spot_creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




# Create your models here.
