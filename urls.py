from django.urls import path
from OTS.views import *
app_name='OTS'

urlpatterns = [
    path('',welcome ),
    path('new-candidate',CandidateRegistrationForm,name='registrationform'),
    path('store-candidate',CandidateRegistration,name='storecandidate'),
    path('login',loginView,name='login'),
    path('home',CandidateHome,name='home'),
    path('test-paper',testPaper,name='testpaper'),
    path('calculate-result',calculateTestResult,name='calculate'),
    path('test-history',testResultHistory,name='testHistory'),
    path('result',showTestResult,name='result'),
    path('logout',logoutView,name='logout'),
]
