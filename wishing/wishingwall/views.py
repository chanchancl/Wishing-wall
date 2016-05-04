from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from datetime import datetime
# Create your views here.
from .models import Wishing

class WishingForm(forms.Form):
    wishingtext = forms.CharField(label='Your Wishing',max_length=254)


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
            if len(text) > 0:
                from django.utils import timezone
                obj = Wishing.objects.create(wID=1,wText=text,wData=timezone.now())
                print(obj)
    form = WishingForm()
    return render(request,'add.html',{'form':form})
    
def delview(request):
    return render(request,'del.html')
    
def test(request):
    #for key in request.session.keys():
    #    print(key,' is ',request.session[key])
    print(request.user)
    return HttpResponse('1')