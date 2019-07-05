from django.db import models

# Create your models here.

class Protocol(models.Model):

    name = models.CharField(
        verbose_name="name of protocol",
        max_length=50,
        null=False,
        blank=False
    )

    number = models.IntegerField(
        verbose_name="protocol number",
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


