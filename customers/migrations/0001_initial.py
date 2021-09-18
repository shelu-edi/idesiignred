# Generated by Django 3.1.2 on 2021-09-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=100)),
                ('salutation', models.CharField(choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('miss', 'Miss')], default='Mr', max_length=10)),
                ('customer_first_name', models.CharField(max_length=500)),
                ('customer_last_name', models.CharField(max_length=500)),
                ('mobile_no', models.IntegerField()),
                ('mobile_no_type', models.CharField(choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('miss', 'Miss')], default='Mobile', max_length=10)),
                ('email', models.EmailField(max_length=120)),
                ('email_type', models.CharField(choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('miss', 'Miss')], default='Work', max_length=10)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]
