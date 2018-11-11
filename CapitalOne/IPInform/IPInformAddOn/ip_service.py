
def record_ip(function):
    def wrap(request, *args, **kwargs):
        print(request.GET.get('test'))
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap