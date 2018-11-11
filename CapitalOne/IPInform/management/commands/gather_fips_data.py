import os
import csv

from django.core.management.base import BaseCommand, CommandError
from census import Census

from ...models import Traffic, FipsData
from django.conf import settings as settings


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the traffic population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Gather fibs for each transaction
        """

        # #Clean up fibs
        # for fib in FipsData.objects.all():
        #     fib.delete()

        ## Load in stats by fibs
        module_dir = os.path.dirname(__file__)
        file_path_edu = os.path.join(module_dir, 'education.csv')

        #Create all fibs models and load in education info
        with open(file_path_edu) as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    fips = row[1]
                    county = row[2]
                    total_population_18_25 = row[3]
                    male_population_18_25 = row[4]
                    female_population_18_25 = row[5]
                    population_18_25_bat_or_up = row[6]
                    population_25_or_up = row[7]
                    population_25_or_up_grad = row[8]
                    # print(fips, county, total_population_18_25, male_population_18_25, female_population_18_25, population_18_25_bat_or_up, population_25_or_up, population_25_or_up_grad)
                    FipsData.objects.create(fips=fips,county=county,total_population_18_25=total_population_18_25,
                                            male_population_18_25=male_population_18_25,female_population_18_25=female_population_18_25,
                                            population_18_25_bat_or_up=population_18_25_bat_or_up,
                                            population_25_or_up=population_25_or_up,
                                            population_25_or_up_grad=population_25_or_up_grad)

        # Create all fibs models and load in income info
        file_path_income = os.path.join(module_dir, 'income.csv')
        with open(file_path_income) as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    t = FipsData.objects.filter(fips=row[1]).first()
                    t.mean_income = row[3]
                    t.save()

        traffic = Traffic.objects.all()
        count = 0
        for t in traffic:
            if not t.fips == 'fips' and FipsData.objects.filter(fips=t.fips).count() > 0 :
                t.fips_data = FipsData.objects.filter(fips=t.fips).first()
                t.save()


