import requests
import time
from numpy import *

from django.core.management.base import BaseCommand, CommandError

from ...models import Traffic, Transaction, FipsData


class MerchantException(Exception):
    def __init__(self):
        Exception.__init__(self, "Error occurred in the traffic population process.")


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Computes score for each fib relative to current transactions
        I am doing a simple normalization and the linearly combining. Might ML weights at a later point.
        """

        transactions = Transaction.objects.all()
        count = 0.0
        total_mean_income=total_population_18_25=total_male_population_18_25=total_female_population_18_25=total_population_18_25_bat_or_up=total_population_25_or_up=total_population_25_or_up_grad=[]
        for t in transactions:
            taff_r = Traffic.objects.filter(ip=t.ip_address.ip).all()
            for traff in taff_r:
                if traff.fips_data and traff.fips_data.mean_income and traff.fips_data.total_population_18_25:
                    count += 1
                    total_mean_income.append(traff.fips_data.mean_income)
                    total_population_18_25.append(traff.fips_data.total_population_18_25)
                    total_male_population_18_25.append(traff.fips_data.male_population_18_25)
                    total_female_population_18_25.append(traff.fips_data.female_population_18_25)
                    total_population_18_25_bat_or_up.append(traff.fips_data.population_18_25_bat_or_up)
                    total_population_25_or_up.append(traff.fips_data.population_25_or_up)
                    total_population_25_or_up_grad.append(traff.fips_data.population_25_or_up_grad)

        for fib in FipsData.objects.all():
            if fib.mean_income:
                income_score = (fib.mean_income - mean(total_mean_income))/std(total_mean_income)
                score_population_18_25 = (fib.total_population_18_25 - mean(total_population_18_25)) / std(total_population_18_25)
                score_male_population_18_25 = (fib.male_population_18_25 - mean(total_male_population_18_25)) / std(total_male_population_18_25)
                score_female_population_18_25 = (fib.female_population_18_25 - mean(total_female_population_18_25)) / std(total_female_population_18_25)
                score_population_18_25_bat_or_up = (fib.population_18_25_bat_or_up - mean(total_population_18_25_bat_or_up)) / std(total_population_18_25_bat_or_up)
                score_population_25_or_up = (fib.population_25_or_up - mean(total_population_25_or_up)) / std(total_population_25_or_up)
                score_population_25_or_up_grad = (fib.population_25_or_up_grad - mean(total_population_25_or_up_grad)) / std(total_population_25_or_up_grad)
                fib.score = abs(income_score+score_population_18_25+score_male_population_18_25+score_female_population_18_25+score_population_18_25_bat_or_up+score_population_25_or_up+score_population_25_or_up_grad)
                fib.save()







