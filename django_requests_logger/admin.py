from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_requests_logger.models import RequestLog


class RequestLogAdmin(admin.ModelAdmin):
    list_display = (
        'url', 'method', 'response_status_code', 'created'
    )
    list_filter = ('method', 'response_status_code')
    search_fields = ['url']
    fieldsets = (
        (None, {
            'fields': (
                'url', 'method', 'response_status_code', 'created')
        }),
        (_('Request'), {
            'classes': ('collapse',),
            'fields': (
                'params', 'body', 'headers')
        }),
        (_('Response'), {
            'classes': ('collapse',),
            'fields': (
                'response_content', 'response_headers')
        })
    )
    readonly_fields = list(d for t in fieldsets for d in t[1]['fields'])


admin.site.register(RequestLog, RequestLogAdmin)
