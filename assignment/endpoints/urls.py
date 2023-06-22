from django.urls import path
from . import views

app_name = 'endpoints'
urlpatterns = [
    path('', views.index, name='index'),
    path('view-1/', views.view_1, name='view_1'),
    path('view-2/', views.view_2, name='view_2')
]