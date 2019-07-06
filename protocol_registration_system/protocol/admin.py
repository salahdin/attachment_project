from django.contrib import admin
from .models import ProtocolResponse,ProtocolRequest
# Register your models here.
admin.site.register(ProtocolRequest)
admin.site.register(ProtocolResponse)