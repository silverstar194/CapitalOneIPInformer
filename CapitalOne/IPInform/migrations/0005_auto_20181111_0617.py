# Generated by Django 2.1.1 on 2018-11-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0004_auto_20181111_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traffic',
            name='fips_data',
        ),
        migrations.AddField(
            model_name='traffic',
            name='fips_data_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
