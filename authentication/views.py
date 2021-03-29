from django.shortcuts import render, HttpResponse, redirect
from .models import Admin
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def register(request):
    fullname = request.POST.get('fullname')
    print(fullname)
    email = request.POST.get('email')
    code = int(request.POST.get('code'))
    phonenumber = int(request.POST.get('phonenumber'))
    job = request.POST.get('job')
    pwd = request.POST.get('password')
    rpwd = request.POST.get('repeatpwd')

    usr = Admin.objects.filter(email=email)
    print(usr)
    if len(usr) == 0:
        if(pwd == rpwd):
            pwd = make_password(pwd)
            newAdmin = Admin.objects.create(fullname=fullname, email=email, code=code, phonenumber=phonenumber,
                                              job=job , pwd=pwd)
            newAdmin.save()
            return render(request , "login.html")
        else:
            return render(request ,'signup.html', {'error': "password does not match"})
    else:
        return render(request, 'signup.html', {'error': 'This user name already exists'})

def login(request):
    return render(request, 'login.html')

def authadmin(request):
    admin = Admin.objects.filter(email=request.POST.get('email')).first()
    if admin is not None:
        if check_password(request.POST.get('password'), admin.pwd):
            request.session['user'] = admin.email
            return render( request , 'index.html')
        else:
            return render(request, 'login.html', {'error': 'invalid password'})
    else:
        return render(request, 'login.html', {'error': 'invalid email id'})

def logout(request):
    del request.session['user']
    return render(request, 'index.html')

def loadtake(request):
    return render(request, 'takeimage.html')

def take(request):
    return HttpResponse('bodfhbdosfvdpsh ')

def adminpanel(request):
    if(request.session.has_key('user')):
        return render(request ,'admin.html')
    else:
        return render(request,'login.html')

def adminuser(request):
    if(request.session.has_key('user')):
        adminData = Admin.objects.all()
        rows = len(adminData)
        # columns = Admin._meta.get_all_field_names()
        return render(request, 'admin.html',{'admindata': adminData,'columns': 'columns'})
    else:
        return render(request,'login.html')

def addadmin(request):
    if (request.session.has_key('user')):
        return render(request,'newadmin.html')
    else:
        return render(request, 'login.html')

def addnewadmin(request):
    if (request.session.has_key('user')):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        code = int(request.POST.get('code'))
        phonenumber = int(request.POST.get('number'))
        job = request.POST.get('job')
        pwd = request.POST.get('password')

        usr = Admin.objects.filter(email=email)
        print(usr)
        if len(usr) == 0:
            pwd = make_password(pwd)
            newAdmin = Admin.objects.create(fullname=fullname, email=email, code=code, phonenumber=phonenumber,
                                            job=job, pwd=pwd)
            newAdmin.save()
            return redirect('/adminuser/')
        else:
            return render(request, 'newadmin.html', {'error': 'This user name already exists'})
    else:
        return render(request,'login.html')

def deleteadmin(request):
    if (request.session.has_key('user')):
        email_list = request.POST.getlist('email_list')
        for email in email_list:
            Admin.objects.get(email=email).delete()
        return redirect('/adminuser/')
    else:
        return render(request,'login.html')
