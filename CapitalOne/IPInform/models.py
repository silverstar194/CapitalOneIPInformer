from django.db import models

# Create your models here.


class Merchant(models.Model):
    '''
    Example from API
    {
      "_id": "57cf75cea73e494d8675ec49",
      "address": {
        "city": "California",
        "state": "CA",
        "street_name": "Apple Campus",
        "street_number": "435",
        "zip": "47389"
      },
      "category": [
        "tech",
        "phones",
        "laptop"
      ],
      "geocode": {
        "lat": 34.98,
        "lng": -79.48
      },
      "name": "Apple"
    },
    '''

    capital_one_id = models.CharField(max_length=64)
    city = models.CharField(max_length=64, blank=True,null=True)
    state = models.CharField(max_length=64, blank=True,null=True)
    street_name = models.CharField(max_length=64, blank=True,null=True)
    street_number = models.IntegerField(blank=True,null=True)
    zip_code = models.IntegerField(blank=True,null=True)
    category = models.CharField(max_length=256, blank=True,null=True)
    lat = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    lng = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    name = models.CharField(max_length=64, blank=True, null=True)


class IPAddress(models.Model):
    ip = models.GenericIPAddressField(protocol='both')


class Traffic(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    lat = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    lng = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    domain = models.CharField(max_length=256, blank=True, null=True)



class Transaction(models.Model):
    from_merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT, related_name="from_merchant")
    to_merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT, related_name="to_merchant")
    ip_address = models.ForeignKey(IPAddress, on_delete=models.PROTECT, related_name="to_address")
    amount = models.DecimalField(decimal_places=6, max_digits=30)
    goods = models.CharField(max_length=64, blank=True, null=True)


