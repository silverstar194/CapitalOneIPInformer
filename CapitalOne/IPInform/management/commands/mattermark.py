import numpy
import requests
import random

from django.core.management.base import BaseCommand, CommandError

from ...models import BusinessInfo
from django.conf import settings as settings


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the transaction population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Generate demo mattermark data
        """

        ##Seed only the best one
        ## Limited to 100 calls
        querystring = {"term": "Whatcom County", "object_types": "company"}
        response = requests.request("GET", settings.API_MATTER_MARK+"/search", params=querystring, headers={'Authorization':settings.API_MATTER_MARK_KEY})

        print(response.text)
        for item in response.json():
            BusinessInfo.objects.create(object_name=item["object_name"],
                                company_domain=item["company_domain"],
                                company_funding=item["company_funding"],
                                company_keywords=item["company_keywords"],
                                company_mattermark_score=item["company_mattermark_score"],
                                object_id=item["object_id"],
                                fips=53073)