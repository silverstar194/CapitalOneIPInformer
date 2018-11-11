from django.http import JsonResponse

from rest_framework.decorators import api_view

from .IPInformAddOn.ip_service import record_ip



@record_ip
@api_view(['GET'])
def make_purchase(request):
    return JsonResponse({"status":"success"})

