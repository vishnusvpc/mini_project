# Generated by Django 4.2.6 on 2023-11-01 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0021_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 11, 1, 15, 39, 54, 812172, tzinfo=datetime.timezone.utc), max_length=20),
        ),
    ]