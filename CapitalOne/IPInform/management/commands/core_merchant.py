from django.core.management.base import BaseCommand, CommandError

from ...models import Merchant


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the merchant population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Create my core merchant for the Capital One account
        """
        if Merchant.objects.filter(pk=9827639).count()  >= 1:
            for m in Merchant.objects.filter(pk=9827639).all():
                m.delete()

        Merchant.objects.create(pk=9827639,
                                capital_one_id="some_dummy_id",
                                city="LA",
                                state="California",
                                street_name="Global Exports Drive",
                                street_number=2394,
                                zip_code=19785,
                                category="Exports and Global Sales",
                                lat=34.0522,
                                lng=118.2437,
                                name="Global Exports Ltd")