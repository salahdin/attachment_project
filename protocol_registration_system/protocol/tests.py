from django.test import TestCase
from .models import ProtocolRequest
from .form import ProtocolForm


class MyTest(TestCase):
    
    def test_ProtocolForm_valid(self):
        form = ProtocolForm(data={'name': "qwert", 'number': "1234", 'description': "sadfasdfasdf", 'pi_email': "salah@gmail.com", 'status':'A'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ProtocolForm_invalid(self):
        form = ProtocolForm(data={'name': "", 'number': "1234", 'description': "sadfasdfasdf", 'pi_email': "salah@gmail.com", 'status':'A'})
        self.assertFalse(form.is_valid())



