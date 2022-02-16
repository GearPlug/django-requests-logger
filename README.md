# django-requests-logger

django-requests-logger is a Django application used as a hook for [Requests](http://docs.python-requests.org/en/master/).

It logs every request made using the Requests library to the database and provides basic data masking for sensitive information.

You can access the logs in the Django admin site.

## Installing
```
pip install django-requests-logger
```

Add `django_requests_logger` in INSTALLED_APPS.

Run `python manage.py migrate`

## Usage
```
import requests
from django_requests_logger.callbacks import logger as requests_logger
from functools import partial

# If you want to capture only errors (HTTP 4XX client errors and 5XX server errors), then pass only_errors argument set to True.

hooks = {"response": partial(requests_logger, only_errors=True)}
requests.get('https://httpbin.org/', hooks=hooks)
```

## TODO
Integrate this application in the Django logging as a handler.

## Requirements
* [Django](https://github.com/django/django)
* [requests](https://github.com/requests/requests)

#### If you want to add yourself some functionality to the application:
1. Fork it ( https://github.com/GearPlug/django-requests-logger )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
