from django.urls import path

from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:kind>/', views.resultJob, name='result'),
    path('dbsetup/', views.dbsetupView, name='dbsetupView'),
    path('dbsetup/setup/', views.insertDataFromCSV, name='dbsetup'),
    path('result1/', views.fir_result, name='result1'),
    path('infojob/', views.wanna_job, name='infojob'),
]
