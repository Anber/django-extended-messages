# Slightly modified django.contrib.messages.api

from django.contrib.messages import constants
from django.contrib.messages.api import get_messages, get_level, set_level, MessageFailure

def add_message(request, level, message, extra_tags='', fail_silently=False, sticky=False):
    """
    Attempts to add a message to the request using the 'messages' app, falling
    back to the user's message_set if MessageMiddleware hasn't been enabled.
    """
    if hasattr(request, '_messages'):
        return request._messages.add(level, message, extra_tags, sticky=sticky)
    if hasattr(request, 'user') and request.user.is_authenticated():
        return request.user.message_set.create(message=message)
    if not fail_silently:
        raise MessageFailure('Without the django.contrib.messages '
                                'middleware, messages can only be added to '
                                'authenticated users.')


def debug(request, message, extra_tags='', fail_silently=False, sticky=False):
    """
    Adds a message with the ``DEBUG`` level.
    """
    add_message(request, constants.DEBUG, message, extra_tags=extra_tags,
                fail_silently=fail_silently, sticky=sticky)


def info(request, message, extra_tags='', fail_silently=False, sticky=False):
    """
    Adds a message with the ``INFO`` level.
    """
    add_message(request, constants.INFO, message, extra_tags=extra_tags,
                fail_silently=fail_silently, sticky=sticky)


def success(request, message, extra_tags='', fail_silently=False, sticky=False):
    """
    Adds a message with the ``SUCCESS`` level.
    """
    add_message(request, constants.SUCCESS, message, extra_tags=extra_tags,
                fail_silently=fail_silently, sticky=sticky)


def warning(request, message, extra_tags='', fail_silently=False, sticky=False):
    """
    Adds a message with the ``WARNING`` level.
    """
    add_message(request, constants.WARNING, message, extra_tags=extra_tags,
                fail_silently=fail_silently, sticky=sticky)


def error(request, message, extra_tags='', fail_silently=False, sticky=False):
    """
    Adds a message with the ``ERROR`` level.
    """
    add_message(request, constants.ERROR, message, extra_tags=extra_tags,
                fail_silently=fail_silently, sticky=sticky)
