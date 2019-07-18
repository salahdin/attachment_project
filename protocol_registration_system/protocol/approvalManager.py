from .models import ProtocolResponse, ProtocolRequest, Protocol
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone


def assignnum():
    ls = [x.number for x in Protocol.objects.all()]
    pro = Protocol.objects.all().last()
    if pro ==  None:
        return 0
    else:
        return pro.id+1


def approve(pq):
    protocol_response = pq.request
    # check if this instance is in the protocol list
    if protocol_response.status == "A":
        return redirect('protocol:protocol-request-list')

    else:
        # change the status of the response to approved
        ProtocolResponse.objects.filter(pk=protocol_response.id).update(status='A')
        # create a protocol instance
        Protocol.objects.create(
            name=pq.name,
            number=assignnum(),
            approval_date=timezone.now(),
            response=protocol_response
        )
        # email.send_email(protocol_request.pi_email,Approved=True,response=True) # send email to pi or user who made the request
        # send email to pi or user who made the request
        return redirect('protocol:protocol-request-list')
