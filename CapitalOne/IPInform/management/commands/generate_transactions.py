import numpy
import os
import random

from django.core.management.base import BaseCommand, CommandError

from ...models import Merchant, Transaction, IPAddress


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the transaction population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Generate demo and test transactions
        """

        ## Clean up transactions
        transactions = Transaction.objects.all()
        for t in transactions:
            t.delete()


        ## Core merchant ID is 9827639
        core_merchant = Merchant.objects.get(id=9827639)

        module_dir = os.path.dirname(__file__)
        file_path_items = os.path.join(module_dir, 'items.txt')
        file_path_ips = os.path.join(module_dir, 'ips.txt')

        with open(file_path_items) as f:
            items = f.readlines()
        items = [x.strip() for x in items]

        with open(file_path_ips) as f:
            ips = f.readlines()
        ips = [x for x in ips]

        merchants = Merchant.objects.all().order_by('?')
        for merchant in merchants[1:150]:
            if merchant == core_merchant:
                pass

            ##Select # items
            mu, sigma = 10, 10
            number_items = abs(int(numpy.random.normal(mu, sigma, 1)))

            ##Generate prices
            mu, sigma = 50, 500
            item_prices = abs(numpy.random.normal(mu, sigma, number_items))


            ##Generate # IPs
            mu, sigma = 2, 15
            num_ips = abs(numpy.random.normal(mu, sigma, 1))
            random.shuffle(ips)
            ips_select = ips[0:int(num_ips)+1]

            for i in range(0,number_items):
                random.shuffle(ips_select)
                random.shuffle(items)
                Transaction.objects.create(
                                from_merchant = merchant,
                                to_merchant = core_merchant,
                                ip_address = IPAddress.objects.create(ip=str(ips_select[0])),
                                amount = item_prices[i],
                                goods = items[0],
                )






