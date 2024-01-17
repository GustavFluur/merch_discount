from django.urls import path

from . import views

app_name = 'merchandise'

urlpatterns = [
    path('newmerch/', views.new_merch, name='new_merch' ),
    path('<int:pk>/', views.merch_detail, name='detail'),

]