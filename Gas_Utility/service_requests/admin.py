from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'request_type', 'status', 'created_at', 'resolved_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'email', 'request_type')

admin.site.register(ServiceRequest, ServiceRequestAdmin)
