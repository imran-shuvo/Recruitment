
from django.urls import path,include
from  . import views

urlpatterns = [
 
    path('sign',views.signMe,name = 'home'),
    path('information',views.applicant_information,name = 'information'),
    path('cv',views.upload_cv)

]
