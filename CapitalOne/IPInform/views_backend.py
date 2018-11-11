import random
import json
from matplotlib import pylab


from django.shortcuts import render
from django.db.models import Count

from rest_framework.decorators import api_view

from .models import Transaction, Merchant, Traffic


@api_view(['GET'])
def index(request):

    ## Transactions
    transactions = Transaction.objects.all()

    merchants =[]
    for t in transactions:
        if not t.from_merchant in merchants:
            merchants.append(t.from_merchant)

    output_mer = []
    mer_lat = []
    mer_lng = []
    for m in merchants:
        mer = {"capital_one_id":m.capital_one_id, "city":m.city, "category":m.category, "name":m.name}
        output_mer.append(mer)
        if m.lat and m.lng:
            mer_lat.append(float(m.lat))
            mer_lng.append(float(m.lng))



    ##Traffic
    ips = Traffic.objects.all()
    output_traff = []
    traff_lat = []
    traff_lng = []
    for ip in ips:
        ## Prevent None colmn
        if ip.name:
            name = ip.name
        else:
            name = ip.ip
        output_traff.append({"city":ip.city, "category":ip.category, "name":name})
        if ip.lat and ip.lng:
            traff_lat.append(float(ip.lat))
            traff_lng.append(float(ip.lng))

    random.shuffle(output_traff)
    output_traff = output_traff[1:len(output_mer)] ## Just tp show data but don't want table going forever
    return render(request, template_name='index.html', context={"transactions":output_mer, "transactions_lat": mer_lat, "transactions_lng": mer_lng, "traffic":output_traff,"traffic_lat":traff_lat,"traffic_lng":traff_lng})



@api_view(['GET'])
def investigate(request):
    pylab
    return render(request, template_name='investigate.html',context={})

