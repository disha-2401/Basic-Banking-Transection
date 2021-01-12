from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('viewProfile/<uid>', views.viewProfile, name='viewProfile'),
    path('transection/<uid>', views.transection, name='transection'),
    path('transferBal/<uid><senderid>', views.transferBal, name='transferBal'),
    path('all_transections',views.all_transections,name='all_transections'),
    path('index', views.index, name='index'),
]