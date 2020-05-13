from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='problems'),
    path('subjects', views.getSubjects, name='subjects'),
    path('testcase', views.getTestCaseInfo, name='testcaseinfo'),
    path('submitans', views.submitAnswer, name='SubmitAnswer')
]
