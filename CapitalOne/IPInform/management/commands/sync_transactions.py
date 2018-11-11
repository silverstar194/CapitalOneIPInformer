import numpy
from decimal import *

from django.core.management.base import BaseCommand, CommandError

from ...models import Transaction, Traffic


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the traffic scatter process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Create traffic for each merchant
        """

        transactions = Transaction.objects.all()

        for t in transactions:
            ip = t.ip_address.ip
            lat = t.from_merchant.lat
            lng = t.from_merchant.lng
            name = t.from_merchant.name
            city = t.from_merchant.city
            category = t.from_merchant.category
            domain = None
            Traffic.objects.create(ip=ip, lat=lat, lng=lng,name=name, city=city, category=category,domain=domain)

