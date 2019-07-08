from django.shortcuts import render,redirect
import datetime 
from .form import ProtocolRequestForm
from .models import *
# Create your views here.
def apply(request):
    passed=False
    if request.method == "POST":
        form = ProtocolRequestForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.request_date=datetime.date.today()#request_date inserted before saving
            post.save()
            passed=True
            return redirect('protocol:apply')
    else:
        form=ProtocolRequestForm()
        return render(request,'protocol/index.html',{'form':form,'passed':passed})

    

   

