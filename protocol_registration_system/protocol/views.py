from django.shortcuts import render,redirect,get_object_or_404
import datetime 
from .form import ProtocolRequestForm
from django.core.mail import send_mail
from django.contrib import messages
from .import email
from .models import ProtocolRequest, ProtocolResponse, Protocol
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



# email api key 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


class ProtocolRequestListView(ListView):
    model = ProtocolRequest
    paginate_by = 5
    context_object_name = 'ProtocolRequest'
    template_name = 'protocol/list.html'


    def get_queryset(self):
        return ProtocolRequest.objects.filter(request_date__lte=datetime.date.today()).order_by('-request_date')[:5]


class ProtocolRequestDetailView(DetailView):

    template_name = 'protocol/detail.html'
    queryset = ProtocolRequest.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ProtocolRequest,id=id_)



def apply(request):
    if request.method == "POST":
        form = ProtocolRequestForm(request.POST)

        if form.is_valid():
            post=form.save(commit=False)
            post.request_date=datetime.date.today()#request_date inserted before saving
            #email.send_email(post.pi_email)
            post.save()
            # create a response for the new
            ProtocolResponse.objects.create(protocolrequest=post,response_date=datetime.date.today())
            messages.success(request, 'Form submission successful!')

            return redirect('protocol:apply')
    else:
        form=ProtocolRequestForm()
        return render(request, 'protocol/index.html', {'form': form})

    
def approve_request(request, id):
    protocol_request = get_object_or_404(ProtocolRequest, pk=id)  # get current request object
    protocol_response = protocol_request.request

    if request.method == 'POST':
        # check if this instance is in the protocol list
        if protocol_response.response is not None:
            messages.success(request, 'already approved')
            return redirect('protocol:protocol-request-list')

        else:
            # change the status of the response to approved
            ProtocolResponse.objects.filter(pk=protocol_response.id).update(status='A')
            # create a protocol instance
            Protocol.objects.create(
                name=protocol_request.name,
                number=13,
                approval_date=datetime.date.today(),
                response=protocol_response
            )
            # email.send_email(protocol_request.pi_email) # send email to pi or user who made the request
            # send email to pi or user who made the request

            return redirect('protocol:protocol-request-list')

    return render(request, 'protocol/detail.html', {'request': protocol_request})

def reject_request(request , id):
    pass










