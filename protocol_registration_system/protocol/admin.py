from django.contrib import admin
from .models import ProtocolResponse, ProtocolRequest,Protocol


class ProtocolResponseInline(admin.TabularInline):
    model = ProtocolResponse


class ProtocolRequestAdmin(admin.ModelAdmin):
    inlines = [ProtocolResponseInline]
    list_display = ('name', 'snippet', 'pi_email', 'request_date')
    list_filter = ['request_date']
    search_fields = ['name']


class ProtocolResponseAdmin(admin.ModelAdmin):
    list_display = ('protocolrequest', 'status')
    list_filter = ['status']

class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'approval_date')
    list_filter = ['approval_date']


admin.site.register(ProtocolRequest, ProtocolRequestAdmin)
admin.site.register(ProtocolResponse, ProtocolResponseAdmin)
admin.site.register(Protocol,ProtocolAdmin)