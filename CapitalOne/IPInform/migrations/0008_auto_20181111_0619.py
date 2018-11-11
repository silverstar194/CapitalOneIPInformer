# Generated by Django 2.1.1 on 2018-11-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0007_auto_20181111_0619'),
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
        migrations.AddField(
            model_name='traffic',
            name='fips_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fips_data', to='IPInform.FipsData'),
        ),
    ]
