from django.db import models
from .ProtocolRequest import *

status_list=(
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('R', 'Rejected')
)


class ProtocolResponse(models.Model):

    protocolrequest = models.OneToOneField(
        ProtocolRequest,
        on_delete=models.CASCADE,
        related_name="request",
        null=True
    )
    status = models.CharField(
        verbose_name="protocol status",
        max_length=50,
        choices=status_list,
        default="P"
    )

    response_date=models.DateField(
        verbose_name="date of response",
    )

    def __str__(self):
        return self.status