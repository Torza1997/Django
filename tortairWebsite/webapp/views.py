from django.http import HttpResponse, HttpResponseRedirect,HttpResponseForbidden
from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse
from django.core import serializers
import json


from datetime import datetime, timedelta

from webapp.models import Table_equipment
from webapp.models import Equipment_detail
from webapp.models import Borrow
from webapp.models import Borro_order
from webapp.models import News

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string as Ran_str
from django.contrib.sessions.backends.db import SessionStore 
from django.contrib import sessions
import random
import qrcode

from webapp.scanqrcode import Borrow_code as br_code
from PIL import Image , ImageDraw

s = SessionStore()
s['check_insert']=''
# link pages*******************************

def index(request):
    return render(request, 'webapp/index.html',{'page_index':1})

def borrow(request):
    s['check'] = 'empty'
    s['scan'] = 'empty'
    s['check_insert'] = ''
    data = Equipment_detail.objects.all()
    if 'search' in request.GET:
        data = ''
        search = request.GET['search']
        data = Equipment_detail.objects.filter(Eqm_ID__Eqm_name__icontains = search)\
             | Equipment_detail.objects.filter(Eqm_ID__Eqm_model__icontains = search)
    request.session[0] = ''
    paginator = Paginator(data, 12)
    num_page = paginator.page_range
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    
    return render(request, 'webapp/contents/fetch.html',{   'data': contacts,
                                                            'num_page':num_page,
                                                        })

@login_required()
def borrow_loing(request,username):
    s['check'] = 'empty'
    s['scan'] = 'empty'
    s['check_insert'] = ''
    data = Equipment_detail.objects.all()
    if 'search' in request.GET:
        data = ''
        search = request.GET['search']
        data = Equipment_detail.objects.filter(Eqm_ID__Eqm_name__icontains = search)\
             | Equipment_detail.objects.filter(Eqm_ID__Eqm_model__icontains = search)
    request.session[0] = ''
    paginator = Paginator(data, 12)
    num_page = paginator.page_range
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    #**********************************
    datas = Borro_order.objects.filter(users = username)
    amount = len(datas)  
    #**********************************
    
    return render(request, 'webapp/contents/fetch.html',{   'data': contacts,
                                                            'num_page':num_page,
                                                            'Amount':amount,
                                                            'pageCheck':'check_1'})

def new_Equipment(request):
    s['check_insert'] = ''
    data = Equipment_detail.objects.all().order_by('-id')[:10]
    news_f = News.objects.all().order_by('-id')[:3]
    return render(request, 'webapp/contents/new_equipment.html',{'data': data,'news_f':news_f})

@login_required()
def Insert_borrow_order(request):
    if request.method == 'POST':
        data = Borro_order.objects.create(
            users = User.objects.get( username = request.POST['username'] ),
            Eqm_name = Table_equipment.objects.get(id = request.POST['ID']),
            Get_Amount = request.POST['Amount'],
            Date_repatriate = request.POST['dates'],
        )
        if s['check'] == 'empty':
            data.save()
        s['check'] = 'not empty'

        #**********************************
        datas = Borro_order.objects.filter(users = request.POST['username'])
        amount = len(datas)  
        #**********************************

    return render(request,'webapp/contents/orderlist.html',{'datas': datas,'Amount':amount,'pageCheck':'check_1'})
    
@login_required()
def Borrow_order(request,username):

    #**********************************
    data = Borro_order.objects.filter(users = username)
    amount = len(data)
    #********************************** 
    
    if amount == 0:
        massage = 'ไม่มีรายการอุปกรณ์ที่ยืม'
        return render(request,'webapp/contents/orderlist.html',{'datas': data,'Amount':amount,'pageCheck':'check_1','massage': massage})  
    else:
        return render(request,'webapp/contents/orderlist.html',{'datas': data,'Amount':amount,'pageCheck':'check_1'})


@login_required()
def insert_borrow(request):
    if request.method == 'POST':
        datass = Borro_order.objects.filter(users = request.POST['username'])

        '''--------ramdom Borrow Code--------'''
        br_code = borrowCode() 
        if not datass:

            #**********************************
            amount = len(datass)  
            #*********************************  

            return render(request,'webapp/contents/orderlist.html',{'datas': datass,'Amount':amount,'pageCheck':'check_1','massage':'ไม่มีรายการอุปกรณ์ที่ยืม'})
        else:
            for data in datass:
                '''-------ลบจากจำนวนที่ยืม-------'''
                Eqm = Table_equipment.objects.get(id = data.Eqm_name.id)
                Amount = data.Get_Amount
                Amounts = Eqm.Amount - Amount

                value = Borrow( First_name = data.users.first_name ,Last_name = data.users.last_name,
                            Eqm_name = data.Eqm_name,Get_Amount = Amount,
                            Br_code = br_code, Date_repatriate =data.Date_repatriate,
                            Get_eqm_id = data.Eqm_name.id,date_br = data.date_br)
                Eqm.Amount = Amounts
                value.save()
                Eqm.save()

            datass.delete()
            img = qrcode.make(br_code)
            draw = ImageDraw.Draw(img)
            draw.text((125,260),text = br_code)
            img.save('webapp/static/include/Qrcode/borrowQR.jpg')
            
            s['Check_username'] = ''

            return render(request, 'webapp/showQrcode.html')


@login_required()
def Allow(request):
    s['scan'] = 'empty'
    s['check_insert'] = ''
    data =  Borrow.objects.filter(Status_borrow = 0)\
            & Borrow.objects.filter(Status_repatriate = 0 )
    if 'search2' in request.GET:
        data = ''
        search = request.GET['search2']
        data =  (Borrow.objects.filter(Br_code__icontains = search)\
                | Borrow.objects.filter(First_name__icontains = search))\
                & Borrow.objects.filter(Status_borrow = 0 )\
                & Borrow.objects.filter(Status_repatriate = 0 )
                
    return render(request, 'webapp/contents/admin.html',{'datas':data,'check_page':1})

@login_required()
def send_borrow(request):
    s['scan'] = 'empty'
    data =  Borrow.objects.filter(Status_borrow = 1)\
            & Borrow.objects.filter(Status_repatriate = 0 )\
            & Borrow.objects.filter(Date_repatriate__gte = datetime.now().date())
    if 'search3' in request.GET:
        data = ''
        search = request.GET['search3']
        data =  (Borrow.objects.filter(Br_code__icontains = search)\
                | Borrow.objects.filter(First_name__icontains = search))\
                & Borrow.objects.filter(Status_borrow = 1)\
                & Borrow.objects.filter(Status_repatriate = 0 )\
                & Borrow.objects.filter(Date_repatriate__gte = datetime.now().date())
    return render(request, 'webapp/contents/admin.html',{'datas':data,'check_page':2})

    
@login_required()
def ScanQrcode_borrow(request):
    data =''
    if s['scan'] == 'empty':
        br_c = br_code()
        if br_c != '0':
            s['get_br_c'] = br_c
            s['scan'] = 'not empty'
            data =  Borrow.objects.filter(Br_code__icontains = s['get_br_c'])\
                    & Borrow.objects.filter(Status_borrow = 0)\
                    & Borrow.objects.filter(Status_repatriate = 0 )
            return render(request, 'webapp/contents/admin.html',{'datas':data,'check':1})
        else:
            s['get_br_c'] = br_c
            return render(request, 'webapp/contents/admin.html',{'datas':data,'check':1})
    else:
        data =  Borrow.objects.filter(Br_code__icontains = s['get_br_c'])\
                & Borrow.objects.filter(Status_borrow = 0)\
                & Borrow.objects.filter(Status_repatriate = 0 )
        return render(request, 'webapp/contents/admin.html',{'datas':data,'check':1})
        
@login_required()
def ScanQrcode_send(request):
    data =''
    if s['scan'] == 'empty':
        br_c = br_code()

        #*******************check page number chang color button************************
        check_date = Borrow.objects.filter(Date_repatriate__lte = datetime.now().date()-timedelta(days=1))\
                     & Borrow.objects.filter(Br_code__icontains = br_c)

        if not check_date:
            check_page = 2
        else:
            check_page = 3
        #********************************************************************************

        if br_c != '0':
            s['get_br_c'] = br_c
            s['scan'] = 'not empty'
            data =  Borrow.objects.filter(Br_code__icontains = s['get_br_c'])\
                    & Borrow.objects.filter(Status_borrow = 1)\
                    & Borrow.objects.filter(Status_repatriate = 0 )
            return render(request, 'webapp/contents/admin.html',{'datas':data,'check':1,'check_page':check_page})
        else:
            s['get_br_c'] = br_c
            return render(request, 'webapp/contents/admin.html',{'datas':data,'check':1,'check_page':check_page})
    else:
        data =  Borrow.objects.filter(Br_code__icontains = s['get_br_c'])\
                & Borrow.objects.filter(Status_borrow = 1)\
                & Borrow.objects.filter(Status_repatriate = 0 )
        return render(request, 'webapp/contents/admin.html',{'datas':data,'check':1,'check_page':check_page})

@login_required()
def detail(request, equipment_id):
    s['check'] = 'empty'
    detail = Equipment_detail.objects.get(id=equipment_id)
    context = {
        'detail': detail,
    }
    return render(request, 'webapp/contents/detail.html', context)


def borrowCode():
    c = True
    while c:
        number = str(random.randint(1000, 9999))
        ran_strs1 = Ran_str(length=3)
        ran_strs2 = Ran_str(length=2)
        borrow_code = ran_strs1+number+ran_strs2
        check = Borrow.objects.filter(Br_code = borrow_code)
        if not check:
            c = False
    return borrow_code

@login_required()
def Update_Status_borrow(request):
    if request.method == "POST":
        status = bool(request.POST['status'])
        ID = int(request.POST['id'])

        status_bor = Borrow.objects.get(id = ID)

        status_bor.Status_borrow = status
        status_bor.save()
        #print("status = %s id = %s" %(status,ID))
        return render(request, 'webapp/contents/admin.html',{'status':status})

@login_required()
def Update_Status_send(request):
    if request.method == "POST":
        status = bool(request.POST['status'])
        ID = int(request.POST['id'])

        status_send = Borrow.objects.get(id = ID)
        Emq_id = status_send.Get_eqm_id
        Eqm = Table_equipment.objects.get(id = Emq_id)

        Amount_T = Eqm.Amount
        Amount_B = status_send.Get_Amount
        Amount_T =  Amount_T + Amount_B
        Eqm.Amount = Amount_T

        status_send.Status_borrow = False
        status_send.Status_repatriate = status
        Eqm.save()
        status_send.save()
       

        #print("status = %s id = %s status_send = %s" %(status,ID,status_send))
        return render(request, 'webapp/contents/admin.html',{'status':status})

@login_required()
def Check_lass_than_date(request):
    data =  Borrow.objects.filter(Date_repatriate__lte = datetime.now().date()-timedelta(days=1))\
            & Borrow.objects.filter(Status_borrow = 1 )\
            & Borrow.objects.filter(Status_repatriate = 0 )
    if 'search4' in request.GET:
        data = ''
        search = request.GET['search4']
        data =  (Borrow.objects.filter(Br_code__icontains = search)\
                | Borrow.objects.filter(First_name__icontains = search))\
                & Borrow.objects.filter(Status_borrow = 1)\
                & Borrow.objects.filter(Status_repatriate = 0 )\
                & Borrow.objects.filter(Date_repatriate__lte = datetime.now().date()-timedelta(days=1))
    return render(request, 'webapp/contents/admin.html',{'datas':data,'check_page':3})

@login_required()
def Getname_list(request):
    data =  Borrow.objects.filter(Status_repatriate = 1)
    return render(request, 'webapp/contents/admin.html',{'datas':data,'check_page':4})

@login_required()
def Update_amount(request,username):
    massege = 'อัพเดทแล้ว'
    check_s = 0
    amount = request.POST['update_mount']
    eqm_id = request.POST['ID']

    if amount > '0' :
        data = Borro_order.objects.get(id = eqm_id)
        data.Get_Amount = amount
        data.save()
    else:
        check_s = 1
        massege = 'จำนวนต้องมากกว่า 0 '
    #**********************************
    data2 = Borro_order.objects.filter(users = username)
    amount = len(data2)
    #********************************** 
    return render(request,'webapp/contents/orderlist.html',{'datas': data2,'Amount':amount,
                                                            'pageCheck':'check_1','massege': massege,
                                                            'check_s': check_s})
@login_required()                                                            
def Delete(request,username):
    check_s = 1
    massege = 'Borrow order Id '+request.POST['ID']+' ถูกลบแล้ว'
    delate_order = Borro_order.objects.filter(id = request.POST['ID'])
    if not delate_order:
        pass
    else:
        delate_order.delete()
    #**********************************
    data2 = Borro_order.objects.filter(users = username)
    amount = len(data2)
    #********************************** 
    return render(request,'webapp/contents/orderlist.html',{'datas': data2,'Amount':amount,
                                                            'pageCheck':'check_1','massege': massege,
                                                            'check_s': check_s})

def Announce(request):
    head = request.POST['head']
    body = request.POST['body']
    if s['check_insert']  == '':
        news_s = News.objects.create(head = head,body = body)
        news_s.save()
    else:
        pass
    s['check_insert'] = 'no empty'
    data = Equipment_detail.objects.all().order_by('-id')[:10]
    news_f = News.objects.all().order_by('-id')[:3]
    return render(request, 'webapp/contents/new_equipment.html',{'data': data,'news_f':news_f})
  
def Feth_announce(request):
    news_ss = News.objects.all().order_by('-id')
    return render(request, 'webapp/contents/new_equipment.html',{'news_ss':news_ss,'page_news':1})
# ***********************************************
