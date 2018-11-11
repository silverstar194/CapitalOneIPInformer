import requests
import time

from django.core.management.base import BaseCommand, CommandError

from ...models import Traffic
from django.conf import settings as settings


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the traffic population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Gather fibs for each transaction
        """

        traffic = Traffic.objects.all()

        count = 0
        for t in traffic:
            time.sleep(.1)
            print(count, traffic.count(), str(((traffic.count()-count)*.1)/60.0)+" min")
            count += 1
            if t.lat and t.lng:
                res = requests.get(url=settings.API_FIBS + "?lat=" +str(float(t.lat))+"&lon="+str(float(t.lng)))
                if res.status_code == 200:
                    if "results" in res.json():
                        if len(res.json()["results"]) > 0:
                            print("Found", res.json()["results"][0]['county_fips'])
                            t.fips = int(res.json()["results"][0]['county_fips'])
                            t.save()
