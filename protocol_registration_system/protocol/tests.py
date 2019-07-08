from django.test import TestCase
from .models import ProtocolRequest
from .form import ProtocolRequestForm


class MyTest(TestCase):
    
    def test_ProtocolRequestForm_valid(self):
        form = ProtocolRequestForm(data={'name': "qwert", 'description': "sadfasdfasdf", 'pi_email': "salah@gmail.com", 'request_date':'2019-02-02'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ProtocolRequestForm_invalid(self):
        form = ProtocolRequestForm(data={'name': "", 'description': "sadfasdfasdf", 'pi_email': "salah@gmail.com", 'request_date':'A'})
        self.assertFalse(form.is_valid())
    # testing email validator
    def test_ProtocolRequestForm_with_invalid_email(self):
        form = ProtocolRequestForm(data={'name': "qwert", 'description': "sadfasdfasdf", 'pi_email': "salah"})
        self.assertFalse(form.is_valid())

