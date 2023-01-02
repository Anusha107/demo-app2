from django.shortcuts import render
from .models import Companyreg
from .models import Add_company

# Create your views here.



def companylogin(request):
    dd = request.POST['id']
    password = request.POST['password']
    qs = Companyreg.objects.filter(userid=dd,password=password)
    if qs:
        return render(request,"admin_login.html")
    else:
        return render(request,'index.html',{'msg':"ivalid login"})

def add_company(request):
    name=request.POST['name']
    symbol=request.POST['symbol']
    password=request.POST['password']
    email =request.POST['email']
    address=request.POST['address']
    phonenumber=request.POST['phonenumber']
    select=request.POST['select']
    image=request.FILES['image']

    qs=Add_company(name=name,symbol=symbol,password=password,email=email,address=address,phonenumber=phonenumber,select=select,image=image)
    qs.save()
    return render(request,"add_company.html",{'msg':"company added sucessfully"})



