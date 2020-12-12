from .models import RecruitmentInfo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class FormRecruitmentInfo(forms.ModelForm):
    class Meta :
        model = RecruitmentInfo
        fields = ['name','email','phone','full_address','name_of_university','graduation_year','cgpa','experience_in_months','current_work_place_name',
        'applying_in','expected_salary','field_buzz_reference','github_project_url','cv_file']

