# Generated by Django 3.1.2 on 2021-09-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sewing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_received', models.DateField()),
                ('date_order_delivered', models.DateField()),
                ('style_no', models.CharField(max_length=1000)),
                ('order_no', models.CharField(max_length=1000)),
                ('remarks', models.CharField(max_length=9000)),
                ('required_date', models.DateField()),
                ('order_accepted', models.BooleanField(default=False)),
                ('order_progress', models.CharField(max_length=1000)),
                ('completed_date', models.DateField()),
                ('release_date', models.DateField()),
                ('reason', models.CharField(max_length=1000)),
            ],
        ),
    ]
