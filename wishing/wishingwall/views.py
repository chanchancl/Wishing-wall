from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.utils import timezone
# Create your views here.
from .models import Wishing
from hashlib import md5
from random import randint

class WishingForm(forms.Form):
    wishingtext = forms.CharField(label='Your Wishing',max_length=254)
    password = forms.CharField(label='删除咒语',max_length=32)

class DelForm(forms.Form):
    id = forms.IntegerField(label='删除的ID')
    password = forms.CharField(label='删除咒语',max_length=32)
    
def index(request):
    objects = Wishing.objects.order_by('wID').reverse()[:5]
    Content = {}
    wishings = []
    for obj in objects:
        wishings.append({"id":obj.wID,
        "text": obj.wText,
        "date": obj.wData,
        })
    
    print(wishings)
    Content = {
        'wishings':wishings
    }
    return render(request,'index.html',Content)
    
def addview(request):
    if request.method == 'POST':
        form = WishingForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['wishingtext']
            password = form.cleaned_data['password']
            if len(text) > 0:
                if len(password) == 0:
                    password = str(randint(0,100000000000))
                else:
                    password = md5(password.encode('gb2312')).hexdigest()
                obj = Wishing.objects.create(wID=1,wText=text,wData=timezone.now(),wPassword=password)
                #print(form.fields)
                print(form.cleaned_data)
                print(form)
    form = WishingForm()
    return render(request,'add.html',{'form':form})
    
def delview(request):
    if request.method == 'POST':
        form = DelForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            objs = Wishing.objects.filter(wID=id)
            
            if objs:
                delnum = 0
                md5Pass = md5(password.encode('gb2312')).hexdigest()
                for obj in objs:
                    if obj.wPassword == md5Pass:
                        obj.delete()
                        delnum += 1
                        
            
            print("Want to del id : ",id,' and password is : ',password)
    form = DelForm()
    return render(request,'del.html',{'form':form})
    
def test(request):
    #for key in request.session.keys():
    #    print(key,' is ',request.session[key])
    print(request.user)
    return HttpResponse('1')