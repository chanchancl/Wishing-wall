from django.shortcuts import render

# Create your views here.
from .models import Wishing

def index(request):
    if request.method == 'POST':
        # 有POST请求
        text = request.POST['wishingText']
        print(text)

        return
    return render(request,'index.html')
    
def addview(request):
    return render(request,'add.html')
    
def delview(request):
    return render(request,'del.html')