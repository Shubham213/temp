# Generated by Django 2.0.2 on 2019-10-29 18:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racerfly', '0005_itemtobuy_order_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totPrice', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('items', models.ManyToManyField(blank=True, null=True, related_name='choice_cart', to='racerfly.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='carts',
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice_users', to='racerfly.Item'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_users', to='racerfly.Order'),
        ),
        migrations.AlterField(
            model_name='itemtobuy',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 23, 42, 54, 519051)),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='choice_order', to='racerfly.ItemToBuy'),
        ),
    ]
