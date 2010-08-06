django-extend-messages
======================

Installation
------------

1. Add "django-extend-messages" directory to your Python path
2. Add *'django.contrib.messages'*
3. Add *'django.contrib.messages.middleware.MessageMiddleware'* to your MIDDLEWARE_CLASSES
4. Add *'django.contrib.messages.context_processors.messages'* to your TEMPLATE_CONTEXT_PROCESSORS
5. Add *MESSAGE_STORAGE = 'extend_messages.storage.session.SessionStorage'* to your settings.py
6. Add *extend_messages.urls* in your urls.py

Configuration
-------------

*STICKY_FROM_THE_LEVEL*

Usage
-----

    import extend_messages as messages
    messages.warning(request, 'Your account expires in three days.', sticky=True)

