from django.db import models
from .ProtocolResponse import ProtocolResponse
from .ProtocolRequest import ProtocolRequest
from  ..validators import *

class Protocol(models.Model):

    name = models.CharField(
        verbose_name="protocol name",
        max_length=50
    )

    number = models.IntegerField(
        verbose_name="assigned protocol number",
        null=False,
        blank=True,
        validators=[validate_protocol_number]
    )

    approval_date = models.DateTimeField(
        verbose_name="date of approval",
        null=False,
    )

    response = models.OneToOneField(
        ProtocolResponse,
        on_delete=models.CASCADE,
        related_name="response",
    )

