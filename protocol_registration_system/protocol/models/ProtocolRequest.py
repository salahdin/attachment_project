from django.db import models


class ProtocolRequest(models.Model):

    # email api key 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
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
    )

    pi_email = models.EmailField(
        verbose_name="PI email",
        max_length=200,
        null=False,
        blank=False,
    )

    request_date = models.DateField(
        verbose_name="requested date"
    )

    def __str__(self):
        return self.name




