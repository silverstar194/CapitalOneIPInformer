# Generated by Django 2.1.1 on 2018-11-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0002_auto_20181110_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='category',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='state',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='street_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]