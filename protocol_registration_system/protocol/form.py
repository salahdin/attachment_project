from django import forms
from .models import ProtocolRequest



class DateInput(forms.DateInput):
    input_type = 'date'

class ProtocolRequestForm(forms.ModelForm):


    class Meta:
        model=ProtocolRequest
        fields=['name', 'description', 'email', 'pi_email', 'durationFrom', 'durationUpto']
        widgets = {
            'durationFrom': DateInput(),
            'durationUpto': DateInput(),
        }
