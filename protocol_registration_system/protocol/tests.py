from django.test import TestCase
from .models import *
from .form import ProtocolRequestForm
from django.urls import reverse


def create_request(self):
    return ProtocolRequest.objects.create(name="abc",
                                          description="abc",
                                          email="abc@gmail.com", pi_email="abc@gmail.com", request_date="2019-02-02")


def create_response(self):
    return ProtocolResponse.objects.create(protocolrequest=create_request(self),
                                           status="P",
                                           response_date="2019-02-02"
                                           )


class ProtocolRequestTest(TestCase):
    
    def test_ProtocolRequestForm_valid(self):
        form = ProtocolRequestForm(data={'name': "qwert", 'description': "sadfasdfasdf",'email':"salah@gmail.com",
                                         'pi_email': "salah@gmail.com", 'request_date': '2019-02-02'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ProtocolRequestForm_invalid(self):
        form = ProtocolRequestForm(data={'name': "", 'description': "sadfasdfasdf",'email':"salah@gmail.com",
                                         'pi_email': "salah@gmail.com", 'request_date': 'A'})
        self.assertFalse(form.is_valid())

    # testing email validator
    def test_ProtocolRequestForm_with_invalid_email(self):
        form = ProtocolRequestForm(data={'name': "qwert", 'description': "sadfasdfasdf", 'pi_email': "salah"})
        self.assertFalse(form.is_valid())


class ProtocolApprovalTest(TestCase):

    # creating a protocol request object
    def setUp(self):
        pass
    # testing if instant of type ProtocolRequest has been created
    def test_request_creation(self):
        a=create_request(self)
        self.assertTrue(isinstance(a, ProtocolRequest))

    def test_response_creation(self):
        a=create_response(self)
        self.assertTrue(isinstance(a, ProtocolResponse))

    # testing if all the protocol instances are approved
    def test_request_approval(self):
        [self.assertEqual(x.response.status, "A") for x in Protocol.objects.all()]

    def test_duplicate_protocol_number(self):
        no_dup=set()
        a=Protocol.objects.all()
        for i in a:
            no_dup.add(i.number)
        self.assertEqual(no_dup,len(a))



class ProtocolRequestDetailViewTests(TestCase):

    def test_detail_for_existing_request(self):
        req = create_request(self)
        url = reverse('protocol:protocol-request-detail', args=(req.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # tests if page return a 404
    def test_detail_for_non_existing_request(self):
        req = create_request(self)
        url = reverse('protocol:protocol-request-detail', args=(req.id+1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)




