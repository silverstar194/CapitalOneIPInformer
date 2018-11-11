import random
import pandas
import json
import numpy
import re
from sklearn.cluster import DBSCAN


from django.shortcuts import render
from django.db.models import Sum

from rest_framework.decorators import api_view

from .models import Transaction, Merchant, Traffic, FipsData, BusinessInfo
from .utils import compute_distance, get_centermost_point


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
    traffic = Traffic.objects.all()[1:100]
    merchants = Merchant.objects.all()[1:100]

    output_lat = []
    output_lng = []
    for t in traffic:
        for m in merchants:
           if compute_distance(t.lat, t.lng, m.lat, m.lng) < 100:
                continue
        if t.lat and t.lng:
            output_lat.append(float(t.lat))
            output_lng.append(float(t.lng))


    ##Cluster points
    df = pandas.DataFrame({'lat': output_lat, 'lng': output_lng})
    coords = df.as_matrix(columns=['lat', 'lng'])

    kms_per_radian = 6371.0088
    eps = 7 / kms_per_radian
    db = DBSCAN(eps=eps, min_samples=1, algorithm='ball_tree', metric='haversine').fit(numpy.radians(coords))
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels))
    clusters = pandas.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    centermost_points = clusters.map(get_centermost_point)

    ## gather all center points
    center_lat = []
    center_lng = []
    for i in centermost_points:
        center_lat.append(i[0])
        center_lng.append(i[1])

    ##Gather ones just with fips
    center_traffic_points_with_fips = []
    fips_data_center_traffic = []
    center_lat_fips = []
    center_lng_fips = []
    for i in range(0,len(center_lat)):
        center_traffic = Traffic.objects.get(lat=center_lat[i], lng=center_lng[i])
        if center_traffic.fips == "fips": ## Fixed some strange stuff here leaving for reference
            center_traffic.fips = None
            center_traffic.save()
        if center_traffic.fips and center_traffic.ip:
            center_traffic_points_with_fips.append(center_traffic)
            center_lat_fips.append(center_lat[i])
            center_lng_fips.append(center_lng[i])
            ## Adds FIPS info
            fips_data = FipsData.objects.filter(fips=center_traffic.fips).first()
            fips_data_center_traffic.append({"data":fips_data, "ip":center_traffic.ip})

    lowest = 10000
    best = None
    for e in fips_data_center_traffic:
        print(e)
        if e["data"]:
            if e["data"].score < lowest:
                lowest = e["data"].score
                best = e

    ##Some more stats
    total_transactions = Transaction.objects.all().count()
    average_cost = float(Transaction.objects.aggregate(Sum('amount'))["amount__sum"])/total_transactions
    total_traffic = Traffic.objects.all().count()
    untapped_traffic = len(output_lat)
    gains = average_cost * (untapped_traffic) * .1  ## 10% gain in conversion



    return render(request, template_name='investigate.html',context={"lat":output_lat, "lng":output_lng,
                                                                     "num_cluser":num_clusters,"center_lat":center_lat,
                                                                     "center_lng":center_lng, "center_lat_fips":center_lat_fips,
                                                                     "center_lng_fips":center_lng_fips,
                                                                     "recommended":center_traffic_points_with_fips[0],
                                                                     "traffic_data":fips_data_center_traffic, "best":best,
                                                                     "total_transactions":total_transactions,
                                                                     "total_traffic":total_traffic,"gains":gains,
                                                                     "untapped_traffic":untapped_traffic, "average_cost":average_cost})


@api_view(['GET'])
def remedy(request, id):
    fips_data = FipsData.objects.filter(fips=id).first()
    trans = Transaction.objects.all()

    tags = {}
    for t in trans:
        m = t.from_merchant
        if m.category:
            categ = json.dumps(m.category)
            categ = re.sub(r'^[a-zA-Z]*$', '', categ)
            if categ in tags:
                tags[categ] = tags[categ] + 1
            else:
                tags[categ] = 1

    leads = BusinessInfo.objects.filter(fips=fips_data.fips).order_by("-company_mattermark_score").all()[1:10] ##Limit for viewing
    return render(request, template_name='remedy.html',context={"fips_data":fips_data, "tags":list(tags.keys())[1:10], "leads":leads}) ##Limit tags to top ones


