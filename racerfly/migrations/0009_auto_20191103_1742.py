# Generated by Django 2.0.2 on 2019-11-03 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racerfly', '0008_auto_20191030_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='itemtobuy',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 17, 42, 15, 144340)),
        ),
    ]
