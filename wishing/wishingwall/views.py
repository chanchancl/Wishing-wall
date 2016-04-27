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