# Generated by Django 2.1.1 on 2018-11-11 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0014_auto_20181110_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='domain',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
