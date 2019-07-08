from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def validate_pi_email(value):
    try:
        EmailValidator(value)
    except ValidationError:
        raise ValidationError('Enter a valid email address.')

    return value
