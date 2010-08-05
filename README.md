django-extend-messages
======================

Installation
------------

1. Add *'django.contrib.messages'*
2. Add *'django.contrib.messages.middleware.MessageMiddleware'* to your MIDDLEWARE_CLASSES
3. Add *'django.contrib.messages.context_processors.messages'* to your TEMPLATE_CONTEXT_PROCESSORS
4. Add *MESSAGE_STORAGE = 'extend_messages.storage.session.SessionStorage'* to your settings.py

Configuration
-------------

*STICKY_FROM_THE_LEVEL*

