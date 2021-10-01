# Generated by Django 3.1.2 on 2021-10-01 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0010_auto_20210929_1728'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ladiesfrock',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='ladiesfrock',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='ladiesfrock',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='ladiesfrock',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='ladiesfrock',
            name='sample_id',
        ),
        migrations.AddField(
            model_name='ladiesfrock',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.ladiesfrock'),
        ),
        migrations.AlterField(
            model_name='ladiesfrock',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
