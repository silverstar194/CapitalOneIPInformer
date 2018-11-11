import numpy
import os
import random
import ipinfo
from decimal import *

from django.core.management.base import BaseCommand, CommandError

from ...models import Traffic
from django.conf import settings as settings


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the traffic population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Scatter city lat and lng
        """


        ## Clean up transactions
        traffic = Traffic.objects.all()

        mu, sigma = .75, .5
        for t in traffic:
            scat = numpy.random.normal(mu, sigma, 2)
            if t.lat and t.lng:
                t.lat += Decimal(scat[0])
                t.lng += Decimal(scat[1])
                t.save()




