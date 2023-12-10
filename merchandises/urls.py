from django.urls import path

from . import views

app_name = 'merchandise'

urlpatterns = [

    path('<int:pk>/', views.merch_detail, name='detail'),

]