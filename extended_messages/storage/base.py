# -*- coding: utf-8 -*-
from random import choice
from django.contrib.messages.storage.base import Message as DjangoMessage, BaseStorage as DjangoBaseStorage
from django.conf import settings


class Message(DjangoMessage):
    """
    Добавляем к стандартному сообщению «липкость».
    Для «липких» сообщений генерируем id.
    """

    def __init__(self, level, message, extra_tags=None, sticky=False):
        super(Message, self).__init__(level, message, extra_tags=extra_tags)
        from_level = getattr(settings, 'STICKY_FROM_THE_LEVEL', None)
        self.sticky = sticky
        if from_level:
            self.sticky = level > from_level
        if self.sticky:
            self.id = ''.join([choice('0123456789abcdef') for i in range(8)])
        else:
            self.id = None


class BaseStorage(DjangoBaseStorage):
    """
    Модернизированное хранилище сообщений.
    """

    def __iter__(self):
        self.used = True
        if self._queued_messages:
            self._loaded_messages.extend(self._queued_messages)
            self._queued_messages = []
        # Загоняем в очередь все «липкие» сообщения
        self._queued_messages = [m for m in self._loaded_messages if m.sticky]
        if self._queued_messages:
            self.added_new = True
        return iter(self._loaded_messages)

    def add(self, level, message, extra_tags='', sticky=False):
        """
        Задействуем нужный Message
        """
        if not message:
            return
        level = int(level)
        if level < self.level:
            return
        self.added_new = True
        message = Message(level, message, extra_tags=extra_tags, sticky=sticky)
        self._queued_messages.append(message)

    def delete(self, id):
        """
        Exclude specified message
        """
        raise NotImplementedError
