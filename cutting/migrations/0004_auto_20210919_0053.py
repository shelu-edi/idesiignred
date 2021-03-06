# Generated by Django 3.1.2 on 2021-09-18 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210918_1525'),
        ('orders', '0004_auto_20210919_0039'),
        ('cutting', '0003_auto_20210916_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recievedin',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='recievedin',
            name='order_no',
        ),
        migrations.RemoveField(
            model_name='sentout',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='sentout',
            name='order_no',
        ),
        migrations.AddField(
            model_name='recievedin',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='recievedin',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.orderreceiving'),
        ),
        migrations.AddField(
            model_name='sentout',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='sentout',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.orderreceiving'),
        ),
    ]
