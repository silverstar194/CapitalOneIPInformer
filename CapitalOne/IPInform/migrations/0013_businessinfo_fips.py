# Generated by Django 2.1.1 on 2018-11-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0012_businessinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='fips',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]