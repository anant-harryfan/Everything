from django.urls import path
from . import views

app_name = 'vidzine'

urlpatterns = [
    path('', views.index, name='index'),
    path('AllVideos/', views.AllVideos, name='discover')
] 