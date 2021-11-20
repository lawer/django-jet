==========
Django JET
==========

[![CodeQL](https://github.com/Onemind-Services-LLC/django-jet/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Onemind-Services-LLC/django-jet/actions/workflows/codeql-analysis.yml) [![Django CI](https://github.com/Onemind-Services-LLC/django-jet/actions/workflows/django.yml/badge.svg)](https://github.com/Onemind-Services-LLC/django-jet/actions/workflows/django.yml) [![Release CI](https://github.com/Onemind-Services-LLC/django-jet/actions/workflows/release-drafter.yml/badge.svg)](https://github.com/Onemind-Services-LLC/django-jet/actions/workflows/release-drafter.yml)

**Modern template for Django admin interface with improved functionality**

Why Django JET?
===============

* New fresh look
* Responsive mobile interface
* Useful admin home page
* Minimal template overriding
* Easy integration
* Themes support
* Autocompletion
* Handy controls

Installation
============

* Download and install latest version of Django JET:

```
    pip install git+https://github.com/Onemind-Services-LLC/django-jet.git
```

* Add 'jet' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

```
    INSTALLED_APPS = (
        ...
        'jet',
        'django.contrib.admin',
    )
```

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+ way):

```
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]
```

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

```
    urlpatterns = patterns(
        '',
        url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
        url(r'^admin/', include(admin.site.urls)),
        ...
    )
```

* Create database tables:

```
    python manage.py migrate jet
```
        
* Collect static if you are in production environment:

```
   python manage.py collectstatic
```
* Clear your browser cache

Dashboard installation
======================

Dashboard is located into a separate application. So after a typical JET installation it won't be active.
To enable dashboard application follow these steps:

* Add 'jet.dashboard' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'jet'):

```
    INSTALLED_APPS = (
        ...
        'jet.dashboard',
        'jet',
        'django.contrib.admin',
        ...
    )
```

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

```
    urlpatterns = patterns(
        '',
        url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
        url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
        url(r'^admin/', include(admin.site.urls)),
        ...
    )
```

* **For Google Analytics widgets only** install python package:

```
    pip install google-api-python-client==1.4.1
```

* Create database tables:

```
    python manage.py migrate dashboard
```

* Collect static if you are in production environment:

```
  python manage.py collectstatic
```
