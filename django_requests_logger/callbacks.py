import json

from django_requests_logger.models import RequestLog


def logger(response, *args, **kwargs):
    if 'application/json' in response.headers['Content-Type']:
        content = response.json()
    else:
        content = response.text

    data = {
        'method': response.request.method,
        'url': response.request.url,
        'params': '',
        'headers': dict(response.request.headers),
        'response_content': content,
        'response_status_code': response.status_code,
        'response_headers': dict(response.headers),
    }
    if response.request.body:
        body = json.loads(response.request.body.decode())
        body = {k: v if not k.startswith('credit_card') else '*****' for k, v in body.items()}
        data['body'] = body

    RequestLog.objects.create(**data)
