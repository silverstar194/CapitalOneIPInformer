# Generated by Django 2.1.1 on 2018-11-10 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IPInform', '0006_auto_20181110_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=6, max_digits=30)),
                ('goods', models.CharField(blank=True, max_length=64, null=True)),
                ('from_merchant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_merchant', to='IPInform.Merchant')),
                ('to_merchant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_merchant', to='IPInform.Merchant')),
            ],
        ),
    ]