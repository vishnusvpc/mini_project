# Generated by Django 4.2.5 on 2023-09-08 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0015_auto_20200516_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 9, 8, 16, 59, 26, 790812, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]
