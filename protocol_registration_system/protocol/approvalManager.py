from .models import ProtocolResponse, ProtocolRequest, Protocol
from django.shortcuts import get_object_or_404, redirect
import datetime


def assignnum():
    ls = [x.number for x in Protocol.objects.all()]
    pro = Protocol.objects.latest('approval_date')
    return pro.id+1


def approve(pk):
    protocol_request = get_object_or_404(ProtocolRequest, pk=pk)  # get current request object
    protocol_response = protocol_request.request

    # check if this instance is in the protocol list
    if protocol_response.status == "A":
        return redirect('protocol:protocol-request-list')

    else:
        # change the status of the response to approved
        ProtocolResponse.objects.filter(pk=protocol_response.id).update(status='A')
        # create a protocol instance
        Protocol.objects.create(
            name=protocol_request.name,
            number=assignnum(),
            approval_date=datetime.datetime.now(),
            response=protocol_response
        )
        # email.send_email(protocol_request.pi_email,Approved=True,response=True) # send email to pi or user who made the request
        # send email to pi or user who made the request
        return redirect('protocol:protocol-request-list')
