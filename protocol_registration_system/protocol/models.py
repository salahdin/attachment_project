from django.db import models

status_list=(
    ('P','Pending'),
    ('A','Approved'),
    ('R','Rejected')
)

class ProtocolResponse(models.Model):
    status = models.CharField(
        verbose_name="protocol status",
        max_length=50,
        choices=status_list,
        default="P"
    )

    number = models.IntegerField(
        verbose_name="assigned protocol number",
        null=False,
        blank=True
    )


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

    pi_email = models.CharField(
        verbose_name="PI email",
        max_length=200,
        null=False,
        blank=False
    )

    request_date = models.DateField(
        verbose_name="requested date"
    )

    response=models.OneToOneField(
        ProtocolResponse,
        on_delete=models.CASCADE,
        related_name="request"
    )

    def __str__(self):
        return self.name


