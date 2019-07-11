from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Protocol

def validate_pi_email(value):
    try:
        EmailValidator(value)
    except ValidationError:
        raise ValidationError('Enter a valid email address.')

    return value

def validate_protocol_number(value):
    list = [x.number for x in Protocol.objects.all()]
    if value in list:
        raise ValidationError('number already taken.')
    else:
        return value