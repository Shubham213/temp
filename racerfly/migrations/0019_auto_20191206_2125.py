# Generated by Django 2.0.2 on 2019-12-06 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racerfly', '0018_auto_20191205_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totPrice',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='itemtobuy',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 6, 21, 25, 3, 310876)),
        ),
    ]
