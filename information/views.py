from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .forms import FormRecruitmentInfo
import requests
from .forms import UserCreateForm
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
import json

token = ''
file_token_id = ''

def applicant_information(request):
    if request.method =='POST':
        form = FormRecruitmentInfo(request.POST)
        global token
        data['token'] = token
        print(form)
        if data.is_valid():
            form.save()
            url = 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'
            headers = {'Authorization':'Token {token}'}
            response = requests.put(url, headers=headers,data=data)
            if response.status_code == 200:
                data = response.json()
                global file_token_id
                file_token_id = data['cv_file'].id
                return Response(data)
        else:
            return HttpResponse("Username or password incorrect")

        # user = authenticate(username=username,password = password)
    else :  
        form = FormRecruitmentInfo()
        context = {'form':form}
        return render(request,'base.html',context)
     


def signMe(request):
    if request.method =='POST':
        # print(request.POST)
        url = 'https://recruitment.fisdev.com/api/login/'
       
        data = json.dumps(request.POST)
        response = requests.post(url, data=data)
        print(response)
        if response.status_code == 200:
            data = response.json()
            global token 
            token= data['token']
            return Response(data, status=status.HTTP_200_OK)
        return HttpResponse('error')
    else :          
        return render(request,'login.html')
             


def upload_cv(request):
    if request.method == "POST": 
        request_file = request.FILES['document'] if 'document' in request.FILES else None
        if request_file: 
            url = 'https://recruitment.fisdev.com/api/file-object/{file_token_id}/'
            data = JSONParser().parse(request_file)
            headers = {'Authorization':'Token {token}'}
            response = requests.put(url, headers=headers,data=data)
            return Response(data)
  
    return render(request, "file.html") 