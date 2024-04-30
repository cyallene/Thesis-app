from django.urls import path
from . import views

app_name = 'thesis'

urlpatterns = [
    path('', views.thesis_list, name='thesis_list'),
    path('detail/<int:thesis_id>/', views.thesis_detail, name='thesis_detail'),
    path('form/', views.thesis_form, name='thesis_form'),
]