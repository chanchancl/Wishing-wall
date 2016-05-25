# -*- UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.utils import timezone
# Create your views here.
from .models import Wishing
from hashlib import md5
from random import randint
import logging
import emoji
import re


logger = logging.getLogger('django.request')

class WishingForm(forms.Form):
    wishingtext = forms.CharField(label='Your Wishing',max_length=254)
    password = forms.CharField(label='删除咒语',max_length=32)

class DelForm(forms.Form):
    wishingid = forms.IntegerField(label='删除的ID')
    password = forms.CharField(label='删除咒语',max_length=32)
    
    
    
def EmojiReplace(string):
    '''
    放这儿做个纪念吧。。。
    这段代码没啥用了
    '''
    pattern = re.compile(r'(?P<a>:[a-zA-Z0-9-+_ ]+:)')
    
    imgTag = '<img src=\"\static\emoji\%s.png\" style=\"width:26.429px\"></img>'
    
    def replace(match):
        print(match.group(0))
        if not emoji.EMOJI_UNICODE.get(match.group(0)):
            return match.group(0)
        text = match.group(0).lstrip(':').rstrip(':')
        tag = imgTag % text
        print(tag)
        return tag
    return pattern.sub(replace,string)
    
    
    
    
    
def GetWishingInfo():
    objects = Wishing.objects.order_by('wID')
    Wishings = []
    
    if objects:
        for obj in objects:
            #text = emoji.demojize(obj.wText)
            #text = EmojiReplace(text)
            #Emoji.replace_unicode(replacement_string)
            Wishings.append({"id":obj.wID,
                "text": obj.wText,
                "date": obj.wData,
            })
        
    return Wishings
    
    
def index(request):
    #objects = Wishing.objects.order_by('wID').reverse()[:5]
    wishings = GetWishingInfo()
    wishings.reverse()
    Content = {
        'wishings':wishings
    }
    return render(request,'index.html',Content)
    
def addview(request):
    Add = False
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
                try:
                    obj = Wishing.objects.create( wID=1,wText=text,wData=timezone.now(),wPassword=password ) 
                except exception as e:
                    logger.debug(str(e))
                Add=True
                #print(form.fields)
                #print(form.cleaned_data)
                #print(form)
                logger.debug(str(form.cleaned_data))
    form = WishingForm()
    return render(request,'add.html',{'form':form,'add':Add})
    
def delview(request):
    Del = False
    if request.method == 'POST':
        form = DelForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['wishingid']
            password = form.cleaned_data['password']
            objs = Wishing.objects.filter(wID=id)
            
            if objs:
                delnum = 0
                md5Pass = md5(password.encode('gb2312')).hexdigest()
                for obj in objs:
                    if obj.wPassword == md5Pass:
                        obj.delete()
                        delnum += 1
                        Del = True
                        
            
            logger.debug("Want to del id : ",id,' and password is : ',password)
    form = DelForm()
    
    wishings = GetWishingInfo()
    wishings.reverse()
    return render(request,'del.html',{'form':form,'wishings':wishings,'del':Del})
    
def test(request):
    #for key in request.session.keys():
    #    print(key,' is ',request.session[key])
    1/0
    print(request.user)
    return HttpResponse('1')