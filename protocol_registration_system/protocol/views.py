from django.shortcuts import render,redirect
import datetime 
from .form import ProtocolRequestForm
from django.core.mail import send_mail
from django.contrib import messages
from .import email
from .models import *
# Create your views here.

# email api key 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
def apply(request):
    passed=False
    if request.method == "POST":
        form = ProtocolRequestForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.request_date=datetime.date.today()#request_date inserted before saving
            """
            send_mail(
                email.req_subject,
                email.req_body,
                "postmaster@sandboxceec9532622a40f297ed91245b14cb8c.mailgun.org",
                [post.pi_email],
                fail_silently=False
            )
            """

            post.save()
            #create a response for the new
            ProtocolResponse.objects.create(response=post,number=00)
            messages.success(request, 'Form submission successful!')

            return redirect('protocol:apply')
    else:
        form=ProtocolRequestForm()
        return render(request, 'protocol/index.html', {'form': form})

    

   

