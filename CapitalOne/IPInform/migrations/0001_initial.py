# Generated by Django 2.1.1 on 2018-11-11 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FipsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.IntegerField(blank=True, null=True)),
                ('mean_income', models.IntegerField(blank=True, null=True)),
                ('total_population_18_25', models.IntegerField(blank=True, null=True)),
                ('female_population_18_25', models.IntegerField(blank=True, null=True)),
                ('male_population_18_25', models.IntegerField(blank=True, null=True)),
                ('population_18_25_bat_or_up', models.IntegerField(blank=True, null=True)),
                ('population_25_or_up', models.IntegerField(blank=True, null=True)),
                ('population_25_or_up_grad', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_one_id', models.CharField(max_length=64)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=64, null=True)),
                ('street_name', models.CharField(blank=True, max_length=64, null=True)),
                ('street_number', models.IntegerField(blank=True, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=256, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=30, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=30, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=30, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=30, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('category', models.CharField(blank=True, max_length=256, null=True)),
                ('domain', models.CharField(blank=True, max_length=256, null=True)),
                ('fips', models.IntegerField(blank=True, null=True)),
                ('fips_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fibs', to='IPInform.FipsData')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=6, max_digits=30)),
                ('goods', models.CharField(blank=True, max_length=64, null=True)),
                ('from_merchant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_merchant', to='IPInform.Merchant')),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_address', to='IPInform.IPAddress')),
                ('to_merchant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_merchant', to='IPInform.Merchant')),
            ],
        ),
    ]
