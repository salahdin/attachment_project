from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Protocol
import datetime

def validate_pi_email(value):
    try:
        EmailValidator(value)
    except ValidationError:
        raise ValidationError('Enter a valid email address.')

    return value

def validate_protocol_number(value):
    lst = [x.number for x in Protocol.objects.all()]
    if value in lst:
        raise ValidationError('number already taken.')
    else:
        return value

def validate_protocol_request_dateupto(value):
    if value < datetime.date.today():
        raise ValidationError('invalid date.')
    else:
        return value