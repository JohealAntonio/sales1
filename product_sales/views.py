from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import HttpResponseRedirect
from .forms import CustomUserCreationForm
#from django.middleware.csrf import _get_new_csrf_token
from django.views.decorators.csrf import csrf_exempt,requires_csrf_token
import cgi
import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime as dt
import pyautogui
import js2py
import json
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from flask import Flask, request, url_for
import random
from django.db import IntegrityError
from django.db import ProgrammingError

# def signup(request):
#     ttl = 'Create a user account'
#     if request.user.is_authenticated:
#         return redirect('signin')
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/index/login')
#         else:
#             return render(request, 'create_acc.html', {'form': form, 'ttl':ttl})
#     else:
#         form = CustomUserCreationForm()
#         return render(request, 'create_acc.html', {'form': form, 'ttl':ttl})

con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS messages(id int NOT NULL AUTO_INCREMENT, first_name varchar(255), last_name varchar(255), email varchar(255), phone_no varchar(255), msg_from varchar(255),  message text,  date varchar(255),  time varchar(255), PRIMARY KEY (id));")
con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS offer(id int NOT NULL AUTO_INCREMENT, service_no varchar(255), service_date varchar(255), service_time varchar(255), cstr_name varchar(255), cstr_mobile_no varchar(255), cstr_email varchar(255), electronics_type varchar(255), brand varchar(255), model_no varchar(255), reason_for_service varchar(255), other_reason varchar(255), address varchar(255), city varchar(255), invoice_no varchar(255),  PRIMARY KEY (id));")
con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS cstr_invoices(id int NOT NULL AUTO_INCREMENT, service_no varchar(255), invoice text, PRIMARY KEY (id));")
con.commit()

cur.close()
con.close()
    
def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

<<<<<<< HEAD
        # Your permission assignment code
        if (position == 'Managing Director') and form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            
            user = User.objects.create_user(username=username, password=password)

            all_permissions = Permission.objects.all()
            user.user_permissions.set(all_permissions)

            # Save the user
            user.save()
            form.save()

            form = AuthenticationForm()
            ttl = 'Login here'
            return render(request, 'employee_login.html', {'form': form, 'ttl':ttl})
=======
>>>>>>> 993392c302719894f7b6e2796dba124fef9dde0a
        

        if form.is_valid():
            try:
                position = request.POST['psn']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                fname = form.cleaned_data['first_name']
                lname = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                codename = ['add_logentry','change_logentry','delete_logentry','view_logentry','add_permission','change_permission',]


                if position == 'Managing Director':
                    user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email, is_superuser = 1)
                    all_permissions = Permission.objects.filter(name=all)
                    user.user_permissions.set(all_permissions)

                elif position == 'Employee':
                    user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email, is_staff = 1)
                    permissions = Permission.objects.filter(codename__in=['view_session', 'delete_session', 'change_session', 'add_session', 'view_contenttype', 'delete_contenttype', 'change_contenttype', 'add_contenttype'])
                    user.user_permissions.set(permissions)

                # Save the user
                user.save()
                form.save()
                    
                return redirect('http://127.0.0.1:8000/loginpage/')
            
            except IntegrityError as e:
                return redirect('http://127.0.0.1:8000/loginpage')
    
    title = 'Create a user account'
    return render(request, 'create_acc.html', {'form': form, 'ttl': title})

def msgs(request): 
    return render(request, 'employee_messages.html')

def imptudts(request): 
    
    if request.user.is_authenticated:
        return render(request, 'employee_updates.html')
    else:
        return redirect('http://127.0.0.1:8000/loginpage/')
    
def getdnm():
    con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
    cur = con.cursor()

    cur.execute("SELECT `service_date` FROM offer")
    dates = [row[0] for row in cur.fetchall()]
    
    s = []
    m = []
    for j in dates:
        s.append(int('{:%d}'.format(dt.strptime(j, '%Y-%m-%d'))))
        m.append(int('{:%m}'.format(dt.strptime(j, '%Y-%m-%d'))))

    cur.close()
    con.close()

    return dates,s,m

def getofrinfo():
    con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
    cur = con.cursor()

    cur.execute("SELECT service_no,service_date,service_time,cstr_name,cstr_mobile_no,cstr_email,electronics_type,brand,model_no,reason_for_service,other_reason,address,city FROM offer ORDER BY `service_date`;")
    columns = [col for col in list(zip(*cur.description))[0]]
    allinfo = cur.fetchall()
    cur.close()
    con.close()
    return json.dumps([dict(zip(columns, row)) for row in allinfo])
    

def offers(request): 
    if request.user.is_authenticated:
        return render(request, 'employee_offers.html',{'info':getofrinfo()})
    else:
        return redirect('http://127.0.0.1:8000/loginpage/')

# def actv_dates():
#     date = getdates()
#     day_lists = [str(i) for i in range(1,32)]

#     for k in day_lists:
#         for j in date:
#             s = '{:%d}'.format(dt.strptime(j, '%Y-%m-%d'))
#             if (k == s):
#                 c = '''let day = document.getElementById("grditm").innerHTML;let con = document.querySelector(".grid-item");if (days==%s){con.className += " actv};'''% s 
#                 return c

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'employee_dashboard.html', {'days':getdnm()[1], 'months':getdnm()[2]})
    else:
        return redirect('http://127.0.0.1:8000/loginpage/')

def md_dashboard(request):
    # if request.user.is_authenticated:
        return render(request, 'md_dashboard.html', {'days':getdnm()[1], 'months':getdnm()[2]})
    # else:
    #     return redirect('http://127.0.0.1:8000/loginpage/')    

# def register_user(request):
#     context = {}
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = CustomUserCreationForm(auto_id=False)
#     context['form'] = form
#     return render_to_response('templates/signup.html',context)
#@_get_new_csrf_token
@csrf_exempt


def user_logout(request):
    requires_csrf_token
    logout(request)
    return render(request,'home.html')
    
def csrf_failure(request, reason=""):
    return render('403_csrf.html')

def index(request):
    if request.method == 'POST':

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        msg_from = request.POST['msg_from']
        msg = request.POST['msg']
        date = request.POST['dt']
        time = request.POST['tm']

        if (fname != '' and lname != '' and email != '' and phone_no != '' and msg != ''):
            con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
            cur = con.cursor()

            cur.execute("INSERT INTO messages (`first_name`,`last_name`,`email`,`phone_no`,`msg_from`,`message`,`date`,`time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(fname,lname,email,phone_no,msg_from,msg,date,time))
            con.commit()
            
            cur.close()
            con.close()

            return render(request, 'index.html')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def lgn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        ttl = 'Login here'
        if user is not None:
            login(request, user)
            return redirect('/employee/dashboard/')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form':form, 'msg':msg, 'ttl':ttl})
    else:
        form = AuthenticationForm()
        ttl = 'Login here'
        return render(request, 'login.html', {'form': form, 'ttl':ttl})
    
def getmsgs():
    con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
    cur = con.cursor()

    cur.execute("SELECT * FROM messages;")
    columns = [col for col in list(zip(*cur.description))[0]]
    allinfo = cur.fetchall()
    cur.close()
    con.close()
    return json.dumps([dict(zip(columns, row)) for row in allinfo])

def msgs_wq(request):
    if request.user.is_authenticated:
        return render(request, 'employee_messages_wq.html', {'msginfo':getmsgs()})
    else:
        return redirect('http://127.0.0.1:8000/loginpage/')
      
def msgs_cg(request):
    if request.user.is_authenticated:
        return render(request, 'employee_messages_cg.html')
    else:
        return redirect('http://127.0.0.1:8000/loginpage/')
  
def msgs_bs(request):
    if request.user.is_authenticated:
        return render(request, 'employee_messages_bs.html')
    else:
        return redirect('http://127.0.0.1:8000/loginpage/')

def lgtpg(request):
    logout(request)
    return render(request, 'logoutpg.html')

def cost(b):
    if b == 'Iphone' or b == 'iphone':
        c = '₹1500' 
        return c 
    else:
        c = '₹500' 
        return c
    
def pccost(b):
    if b == 'Macbook' or b == 'iMac' or b=='Mac':
        c = '₹5500' 
        return c 
    else:
        c = '₹2500' 
        return c

def raninvno():
    r1 = random.randint(10000000,100000000)
    s1 = "#"+str(r1)
    return s1

ino = raninvno()

def invoice(request):
    cname = request.GET.get('cname')
    cmno = request.GET.get('cmno')
    addr = request.GET.get('addr')
    cty = request.GET.get('cty')
    ror = request.GET.get('ror')
    cst = request.GET.get('cst')
    etype = request.GET.get('etype')
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    date = request.GET.get('date')

    return render(request, 'invoice.html', {
        'cname': cname,
        'cmno': cmno,
        'addr': addr,
        'cty': cty,
        'ror': ror,
        'cst': cst,
        'etype': etype,
        'brand': brand,
        'model': model,
        'date': date,
        'ino':ino,
    })
    

def msbkg(request):
    if request.method == 'POST':
        sno=request.POST['service_no']
        sdate=request.POST['service_date']
        stime=request.POST['service_time']
        cname=request.POST['cstr_name']
        cmno=request.POST['cstr_mobile_no']
        cemail=request.POST['cstr_email']
        dtype=request.POST['device_type']
        dbrd=request.POST['device_brand']
        dmdl=request.POST['device_model']
        ror=request.POST['reason_of_repair']
        otr=request.POST['other_reason']
        addr=request.POST['address']
        cty=request.POST['city']

        con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
        cur = con.cursor()

        cur.execute("INSERT INTO offer (`service_no`, `service_date`, `service_time`, `cstr_name`, `cstr_mobile_no`, `cstr_email`, `electronics_type`, `brand`, `model_no`, `reason_for_service`, `other_reason`, `address`, `city`,`invoice_no`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sno,sdate,stime,cname,cmno,cemail,dtype,dbrd,dmdl,ror,otr,addr,cty,ino))
        con.commit()
         
        
        cur.close()
        con.close()

                    

        
        destination_url = reverse('invoice')

        # list = [(k, v) for k, v in dict.items()]
        redirect_url = f'{destination_url}?cname={cname}&cmno={cmno}&addr={addr}&cty={cty}&ror={othr(ror,otr)}&cst={cost(dbrd)}&etype={dtype}&brand={dbrd}&model={dmdl}&date={sdate}&ino={ino}'

        con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
        cur = con.cursor()

        cur.execute("INSERT INTO cstr_invoices(`service_no`, `invoice`) VALUES (%s,%s)",(sno,'http://127.0.0.1:8000'+redirect_url))
        con.commit()
        
        
        cur.close()
        con.close()

        return redirect(redirect_url)
        # return redirect('http://127.0.0.1:8000/invoice', kwargs={'cname':cname, 'cmno':cmno, 'addr':addr, 'cty':cty, 'ror':othr(ror,otr), 'cst':cost(dbrd), 'etype':dtype, 'brand':dbrd, 'model':dmdl, 'date':sdate})      
    else:
        return render(request, 'msbooking.html')

def oasbkg(request):
    if request.method == 'POST':

        sno=request.POST['service_no']
        sdate=request.POST['service_date']
        stime=request.POST['service_time']
        cname=request.POST['cstr_name']
        cmno=request.POST['cstr_mobile_no']
        cemail=request.POST['cstr_email']
        dtype=request.POST['device_type']
        dbrd=request.POST['device_brand']
        dmdl=request.POST['device_model']
        ror=request.POST['reason_of_repair']
        otr=request.POST['other_reason']
        addr=request.POST['address']
        cty=request.POST['city']

        con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
        cur = con.cursor()
        
        cur.execute("INSERT INTO offer (`service_no`, `service_date`, `service_time`, `cstr_name`, `cstr_mobile_no`, `cstr_email`, `electronics_type`, `brand`, `model_no`, `reason_for_service`, `other_reason`, `address`, `city`,`invoice_no`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sno,sdate,stime,cname,cmno,cemail,dtype,dbrd,dmdl,ror,otr,addr,cty,ino))
        con.commit()
        
        cur.close()
        con.close()

        
        destination_url = reverse('invoice')

        cst = 'Amount will be discussed on the day of service.'
 
        # list = [(k, v) for k, v in dict.items()]
        redirect_url = f'{destination_url}?cname={cname}&cmno={cmno}&addr={addr}&cty={cty}&ror={othr(ror,otr)}&cst={cst}&etype={dtype}&brand={dbrd}&model={dmdl}&date={sdate}&ino={ino}'

        con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
        cur = con.cursor()

        cur.execute("INSERT INTO cstr_invoices(`service_no`, `invoice`) VALUES (%s,%s)",(sno,'http://127.0.0.1:8000'+redirect_url))
        con.commit()
        
        cur.close()
        con.close()

        return redirect(redirect_url)
    else:
        return render(request, 'oasbooking.html')

def othr(r,o):
    if (r=='Other'):
        return o
    else:
        return r

def csbkg(request):
    if request.method == 'POST':

        sno=request.POST['service_no']
        sdate=request.POST['service_date']
        stime=request.POST['service_time']
        cname=request.POST['cstr_name']
        cmno=request.POST['cstr_mobile_no']
        cemail=request.POST['cstr_email']
        dtype=request.POST['device_type']
        dbrd=request.POST['device_brand']
        dmdl=request.POST['device_model']
        ror=request.POST['reason_of_repair']
        otr=request.POST['other_reason']
        addr=request.POST['address']
        cty=request.POST['city']

        con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
        cur = con.cursor()
        
        cur.execute("INSERT INTO offer (`service_no`, `service_date`, `service_time`, `cstr_name`, `cstr_mobile_no`, `cstr_email`, `electronics_type`, `brand`, `model_no`, `reason_for_service`, `other_reason`, `address`, `city`,`invoice_no`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sno,sdate,stime,cname,cmno,cemail,dtype,dbrd,dmdl,ror,otr,addr,cty,ino))
        con.commit()
        
        cur.close()
        con.close()

        
        destination_url = reverse('invoice')
 
        # list = [(k, v) for k, v in dict.items()]
        redirect_url = f'{destination_url}?cname={cname}&cmno={cmno}&addr={addr}&cty={cty}&ror={othr(ror,otr)}&cst={pccost(dbrd)}&etype={dtype}&brand={dbrd}&model={dmdl}&date={sdate}&ino={ino}'

        con = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')
        cur = con.cursor()

        cur.execute("INSERT INTO cstr_invoices(`service_no`, `invoice`) VALUES (%s,%s)",(sno,'http://127.0.0.1:8000'+redirect_url))
        con.commit()
        
        cur.close()
        con.close()

        return redirect(redirect_url)
    else:
        return render(request, 'csbooking.html')
        

