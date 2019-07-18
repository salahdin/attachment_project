from .models import ProtocolResponse, ProtocolRequest, Protocol
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone


class ApproveProtocol:

    def assign_protocol_number(self):
        """Returns the next available protocol number.

        :return: protocol number
        """
        last_protocol_number = 0
        new_number = 0
        protocol = Protocol.objects.all().order_by('number').last()
        if protocol:
            last_protocol_number = protocol.number
            new_number = last_protocol_number + 1
        else:
            new_number = 1
        return new_number


    def approve(self, protocol_request=None):
        """Returns True if a protocol is approved and creates a protocol instance.

        :param protocol_request:
        :return:
        """
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
                number=self.assign_protocol_number(),
                approval_date=timezone.now(),
                response=protocol_response
            )
            # email.send_email(protocol_request.pi_email,Approved=True,response=True) # send email to pi or user who made the request
            # send email to pi or user who made the request
            return redirect('protocol:protocol-request-list')
