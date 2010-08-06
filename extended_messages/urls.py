from django.conf.urls.defaults import *
from views import delete

urlpatterns = patterns('',
    url(r'^delete/(?P<id>[0-9a-f]{8})/$', delete, name="extended_messages_delete"),
)
