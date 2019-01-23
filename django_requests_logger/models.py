from django.db import models
from django.utils.translation import ugettext_lazy as _


class RequestLog(models.Model):
    method = models.CharField(_('method'), max_length=10, help_text=_('request method'))
    url = models.TextField(_('url'), help_text=_('request url'))
    params = models.TextField(_('parameters'), help_text=_('request params'))
    body = models.TextField(_('body'), help_text=_('request body'))
    headers = models.TextField(_('headers'), help_text=_('request headers'))

    response_content = models.TextField(_('content'), help_text=_('response content'))
    response_headers = models.TextField(_('headers'), help_text=_('response headers'))
    response_status_code = models.CharField(_('status code'), max_length=10, help_text=_('response status code'))

    last_modified = models.DateTimeField(_('last modified'), auto_now=True, help_text=_('last modification date'))
    created = models.DateTimeField(_('created'), auto_now_add=True, help_text=_('creation date'))

    class Meta:
        db_table = 'request_log'
        verbose_name = 'Request Log'
        verbose_name_plural = 'Request Logs'
