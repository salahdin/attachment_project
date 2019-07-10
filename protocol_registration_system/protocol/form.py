from django import forms
from .models import ProtocolRequest

class ProtocolRequestForm(forms.ModelForm):


    class Meta:
        model=ProtocolRequest
        fields=['name', 'description', 'email', 'pi_email',]
