import simplejson
from django.http import HttpResponse, HttpResponseRedirect


def delete(request, id):
    request._messages.delete(id)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(dict(success=True)), mimetype='application/json')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
