# Generated by Django 3.1.2 on 2021-09-18 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210918_1525'),
        ('invoice', '0006_auto_20210919_0039'),
        ('accessories', '0002_auto_20210915_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accrecievedin',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='accrecievedin',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='accrecievedin',
            name='invoice_no',
        ),
        migrations.RemoveField(
            model_name='accsentout',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='accsentout',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='accsentout',
            name='invoice_no',
        ),
        migrations.AddField(
            model_name='accrecievedin',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='accrecievedin',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.invoice'),
        ),
        migrations.AddField(
            model_name='accsentout',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='accsentout',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.invoice'),
        ),
    ]