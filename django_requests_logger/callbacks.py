import json
from urllib.parse import parse_qs

from django_requests_logger.models import RequestLog
from django_requests_logger.signals import response_is_not_ok, response_is_ok


def logger(response, data_masking=None, only_errors=False, *args, **kwargs):
    if only_errors and response.ok:
        return

    if "Content-Type" in response.headers and "application/json" in response.headers["Content-Type"]:
        content = response.json()
    else:
        content = response.text

    data = {
        "method": response.request.method,
        "url": response.request.url,
        "params": "",
        "headers": dict(response.request.headers),
        "response_content": content,
        "response_status_code": response.status_code,
        "response_headers": dict(response.headers),
    }
    if response.request.body:
        try:
            body = json.loads(response.request.body.decode())
        except Exception:
            try:
                body = parse_qs(response.request.body)
            except Exception:
                body = response.request.body

        if data_masking and isinstance(body, dict):
            body = masking(body, data_masking)

        data["body"] = body

    obj = RequestLog.objects.create(**data)
    if response.ok:
        response_is_ok.send(sender=RequestLog, instance=obj)
    else:
        response_is_not_ok.send(sender=RequestLog, instance=obj)


def masking(body, data_masking):
    return {k: "*****" if any((d in k for d in data_masking)) else v for k, v in body.items()}
