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


class FipsData(models.Model):
    fips = models.IntegerField(blank=True,null=True)
    county = models.CharField(max_length=64, blank=True, null=True)
    mean_income = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    total_population_18_25 =  models.IntegerField(blank=True,null=True)
    male_population_18_25 = models.IntegerField(blank=True, null=True)
    female_population_18_25 = models.IntegerField(blank=True, null=True)
    population_18_25_bat_or_up = models.IntegerField(blank=True, null=True)
    population_25_or_up = models.IntegerField(blank=True, null=True)
    population_25_or_up_grad = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)

class BusinessInfo(models.Model):
    fips = models.IntegerField(blank=True, null=True)
    object_name = models.CharField(max_length=64, blank=True, null=True)
    company_domain = models.CharField(max_length=256, blank=True, null=True)
    company_funding = models.IntegerField(blank=True, null=True)
    company_keywords = models.CharField(max_length=256, blank=True, null=True)
    company_mattermark_score = models.IntegerField(blank=True, null=True)
    object_id = models.CharField(max_length=64, blank=True, null=True)


class Traffic(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    lat = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    lng = models.DecimalField(decimal_places=6, max_digits=30, blank=True,null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    domain = models.CharField(max_length=256, blank=True, null=True)
    fips =  models.IntegerField(blank=True,null=True)
    fips_data = models.ForeignKey(FipsData, on_delete=models.PROTECT, related_name="fips_data",null=True)



class Transaction(models.Model):
    from_merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT, related_name="from_merchant")
    to_merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT, related_name="to_merchant")
    ip_address = models.ForeignKey(IPAddress, on_delete=models.PROTECT, related_name="to_address")
    amount = models.DecimalField(decimal_places=6, max_digits=30)
    goods = models.CharField(max_length=64, blank=True, null=True)


