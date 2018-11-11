import numpy
import os
import random
import ipinfo

from django.core.management.base import BaseCommand, CommandError

from ...models import Traffic
from django.conf import settings as settings


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the traffic population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Generate demo and test traffic
        """

        lat = lng = name = city = category = domain = None

        ## Clean up transactions
        traffic = Traffic.objects.all()
        for t in traffic:
            t.delete()

        module_dir = os.path.dirname(__file__)
        file_path_ips = os.path.join(module_dir, 'ips.txt')

        with open(file_path_ips) as f:
            ips = f.readlines()
        ips = [x for x in ips]

        random.shuffle(ips)
        ips = ips[0:300]

        for ip in ips:
            Traffic.objects.create(ip="104.175.221.247")
            access_token = settings.IPINFO_API_KEY
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip)

            if details.latitude:
                lat = details.latitude

            if details.longitude:
                lng = details.longitude

            if 'asn' in details.all:
                if 'name' in details.all['asn']:
                    name = details.all['asn']['name']
            else:
                if 'company' in details.all:
                    if 'name' in details.all['company']:
                        name = details.all['company']['name']

            if details.city:
                city = details.city

            if 'asn' in details.all:
                if 'type' in details.all['asn']:
                    category = details.all['asn']['type']
            else:
                if 'company' in details.all:
                    if 'type' in details.all['company']:
                        category = details.all['company']['type']


            if 'asn' in details.all:
                if 'domain' in details.all['asn']:
                    domain = details.all['asn']['domain']
            else:
                if 'company' in details.all:
                    if 'domain' in details.all['company']:
                        domain = details.all['company']['domain']

            print(lat, lng, name, city, category, domain)

            Traffic.objects.create(ip=ip,
                                   lat=lat,
                                   lng=lng,
                                   name=name,
                                   city=city,
                                   category=category,
                                   domain=domain)




