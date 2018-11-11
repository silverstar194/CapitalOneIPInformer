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

        # ##Seed only the best one
        # ## Limited to 100 calls
        # querystring = {"term": "Whatcom County", "object_types": "company"}
        # response = requests.request("GET", settings.API_MATTER_MARK+"/search", params=querystring, headers={'Authorization':settings.API_MATTER_MARK_KEY})
        #
        # for item in response.json():
        #     BusinessInfo.objects.create(object_name=item["object_name"],
        #                         company_domain=item["company_domain"],
        #                         company_funding=item["company_funding"],
        #                         company_keywords=item["company_keywords"],
        #                         company_mattermark_score=item["company_mattermark_score"],
        #                         object_id=item["object_id"],
        #                         fips=53073)


        for info in BusinessInfo.objects.all():
            response = requests.request("GET", settings.API_MATTER_MARK+"/companies/"+str(info.object_id),headers={'Authorization':settings.API_MATTER_MARK_KEY})
            item = response.json()
            print(item)
            description = item["description"]
            revenue_range = item["revenue_range"]
            if len(item["google_play_apps"]) > 0:
                play_url = item["google_play_apps"][0]["play_url"]
            if len(item["itunes_apps"]) > 0:
                app_name = item["itunes_apps"][0]["itunes_url"]
            info.description = description
            info.revenue_range = revenue_range
            if info.play_url:
                info.play_url = play_url
            if info.app_name:
                info.app_name = app_name
            info.save()
            print("Saved")

