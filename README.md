django-extended-messages
======================

Installation
------------

1. Add *'django-extended-messages'* directory to your Python path
2. Add *'django.contrib.messages'* to your INSTALLED_APPS
3. Add *'django.contrib.messages.middleware.MessageMiddleware'* to your MIDDLEWARE_CLASSES
4. Add *'django.contrib.messages.context_processors.messages'* to your TEMPLATE_CONTEXT_PROCESSORS
5. Add *MESSAGE_STORAGE = 'extended_messages.storage.session.SessionStorage'* to your settings.py
6. Add *extended_messages.urls* in your urls.py

Configuration
-------------

*STICKY_FROM_THE_LEVEL*

Usage
-----

    import extended_messages as messages
    messages.warning(request, 'Your account expires in three days.', sticky=True)

