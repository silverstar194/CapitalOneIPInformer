# Generated by Django 2.1.1 on 2018-11-11 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0002_auto_20181111_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traffic',
            old_name='fibs',
            new_name='fips',
        ),
        migrations.RenameField(
            model_name='traffic',
            old_name='fibs_data',
            new_name='fips_data',
        ),
    ]