from django.contrib import admin
from .models import ProtocolResponse, ProtocolRequest


class ProtocolResponseInline(admin.TabularInline):
    model = ProtocolResponse


class ProtocolRequestAdmin(admin.ModelAdmin):
    inlines = [ProtocolResponseInline]
    list_display = ('name', 'description', 'pi_email', 'request_date')
    list_filter = ['request_date']
    search_fields = ['name']


class ProtocolResponseAdmin(admin.ModelAdmin):
    list_display = ('response', 'status')
    list_filter = ['status']


admin.site.register(ProtocolRequest, ProtocolRequestAdmin)
admin.site.register(ProtocolResponse, ProtocolResponseAdmin)