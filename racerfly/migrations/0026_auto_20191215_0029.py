# Generated by Django 2.1.7 on 2019-12-14 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racerfly', '0025_auto_20191213_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemtobuy',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 0, 29, 16, 736531)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggested_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 0, 29, 16, 744731)),
        ),
    ]
