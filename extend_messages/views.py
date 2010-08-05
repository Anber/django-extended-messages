from django.http import HttpResponseRedirect


def delete(request, id):
    request._messages.delete(id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
