from django.db import models
from .ProtocolResponse import ProtocolResponse
from .ProtocolRequest import ProtocolRequest


class Protocol(models.Model):

    name=models.CharField(
        verbose_name="protocol name",
        max_length=50
    )

    number = models.IntegerField(
        verbose_name="assigned protocol number",
        null=False,
        blank=True,
    )

    approval_date=models.DateField(
        verbose_name="date of approval",
        null=False,
    )

    response = models.OneToOneField(
        ProtocolResponse,
        on_delete=models.CASCADE,
        related_name="response",
    )

