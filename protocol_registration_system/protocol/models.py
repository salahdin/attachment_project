from django.db import models
from .validators import validate_pi_email


status_list=(
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('R', 'Rejected')
)

# email api key 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
class ProtocolRequest(models.Model):

    name = models.CharField(
        verbose_name="protocol name",
        max_length=50,
        null=False,
        blank=False
    )

    description = models.TextField(
        verbose_name="protocol description",
        max_length=500,
        null=False,
        blank=True
    )

    email = models.EmailField(
        verbose_name="email",
        max_length=200,
        null=False,
        blank=False,
        validators=[validate_pi_email]
    )

    pi_email = models.EmailField(
        verbose_name="PI email",
        max_length=200,
        null=False,
        blank=False,
        validators=[validate_pi_email]
    )

    request_date = models.DateField(
        verbose_name="requested date"
    )

    def __str__(self):
        return self.name


class ProtocolResponse(models.Model):

    response = models.OneToOneField(
        ProtocolRequest,
        on_delete=models.CASCADE,
        related_name="request"
    )
    status = models.CharField(
        verbose_name="protocol status",
        max_length=50,
        choices=status_list,
        default="P"
    )


    def __str__(self):
        return self.status


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











