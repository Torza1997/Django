from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'myapp'
urlpatterns = [
    #test link pages**********************************
    path('',views.index, name = 'index'),
    path('borrow', views.borrow, name='borrow'),
    path('new_equipment/', views.new_Equipment, name='new'),
    path('insert_borrow/', views.insert_borrow, name='insert_borrow'),
    path('borrow/<int:equipment_id>/detail', views.detail, name='detail'),
    path('ScanQrcode_borrow', views.ScanQrcode_borrow, name='ScanQrcode_borrow'),
    path('ScanQrcode_send', views.ScanQrcode_send, name='ScanQrcode_send'),
    url(r'Allow', views.Allow, name='Allow'),
    url(r'Update_Status_borrow', views.Update_Status_borrow, name='Update_Status_borrow'),
    url(r'Update_Status_send', views.Update_Status_send, name='Update_Status_send'),
    url(r'send_borrow', views.send_borrow, name='send_borrow'),
    url(r'Check_lass_than_date',views.Check_lass_than_date ,name='Check_lass_than_date'),
    url(r'Getname_list',views.Getname_list ,name='Getname_list'),
    url(r'borrow/(?P<username>\w+)/$',views.borrow_loing ,name='borrow_loing'),
    url(r'(?P<username>\w+)/Update_amount/$',views.Update_amount ,name='Update_amount'),
    url(r'(?P<username>\w+)/delete/$',views.Delete ,name='Delete'),
    url(r'Borrow_order/(?P<username>\w+)/$',views.Borrow_order ,name='Borrow_order'),
    url(r'Insert_borrow_order',views.Insert_borrow_order ,name='Insert_borrow_order'),
    url(r'Announce/$',views.Announce ,name='Announce'),
    url(r'Announce_all/$',views.Feth_announce ,name='Feth_announce'),
    #path('calendar/', views.calendar, name='calendar'),
    #*************************************************
] 














