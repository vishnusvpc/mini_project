# Generated by Django 4.2.5 on 2023-09-08 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0016_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 9, 8, 17, 4, 4, 315042, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]