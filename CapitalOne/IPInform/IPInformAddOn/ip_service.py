from ..models import Traffic

from ipware import get_client_ip

def record_ip(function):
    def wrap(request, *args, **kwargs):
        client_ip, is_routable = get_client_ip(request)
        Traffic.objects.create(ip=client_ip)
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap