import json
import requests

from django.core.management.base import BaseCommand, CommandError
I
from ...models import Merchant
from django.conf import settings as settings


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the merchant population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Imports all merchants for the Capital One account
        """

        res = requests.get(url=settings.CAPITAL_ONE_API+"merchants/?key="+settings.CAPITAL_ONE_API_KEY)
        for m in res.json():
            capital_one_id = city = state = street_name = street_number = zip_code = category = lat = lng = name = None

            try:
                if "_id" in m:
                    capital_one_id = m["_id"]

                if "address" in m and "city" in m["address"]:
                    city = str(m["address"]["city"])

                if "address" in m and "state" in m["address"]:
                    state = str(m["address"]["state"])

                if "address" in m and "street_number" in m["address"]:
                    street_number = int(m["address"]["street_number"])

                if "address" in m and "zip" in m["address"]:
                    zip_code = int(m["address"]["zip"])

                if "category" in m:
                    category = str(m["category"])

                if "geocode" in m and  "lat" in m["geocode"]:
                    lat = float(m["geocode"]["lat"])

                if "geocode" in m and  "lng" in m["geocode"]:
                    lng = float(m["geocode"]["lng"])

                if "name" in m:
                    name = str(m["name"])
                else:
                    raise MerchantException()
            except Exception as E:
                print(E)
            print(capital_one_id, city, state, street_name, street_number, zip_code, category, lat,lng,name)

            Merchant.objects.create(capital_one_id=capital_one_id,
                                    city=city,
                                    state=state,
                                    street_name=street_name,
                                    street_number=street_number,
                                    zip_code=zip_code,
                                    category=category,
                                    lat=lat,
                                    lng=lng,
                                    name=name)

            ## Remove dups
            count = Merchant.objects.filter(capital_one_id=capital_one_id).count()
            while count >= 1:
                Merchant.objects.filter(capital_one_id=capital_one_id)[0].delete()
                count -= 1