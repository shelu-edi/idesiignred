# Generated by Django 3.1.2 on 2021-10-01 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample', '0010_auto_20210929_1728'),
        ('products', '0002_auto_20211001_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boyspant',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='boyspant',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='boyspant',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='boyspant',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='boyspant',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='boysshirt',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='boysshirt',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='boysshirt',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='boysshirt',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='boysshirt',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='boysshort',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='boysshort',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='boysshort',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='boysshort',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='boysshort',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='boystshirt',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='boystshirt',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='boystshirt',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='boystshirt',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='boystshirt',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='girlsfrock',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='girlsfrock',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='girlsfrock',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='girlsfrock',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='girlsfrock',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='girlspant',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='girlspant',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='girlspant',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='girlspant',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='girlspant',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='girlsshort',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='girlsshort',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='girlsshort',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='girlsshort',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='girlsshort',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='girlstshirt',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='girlstshirt',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='girlstshirt',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='girlstshirt',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='girlstshirt',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='infantsfrock',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='infantsfrock',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='infantsfrock',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='infantsfrock',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='infantsfrock',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='infantspant',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='infantspant',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='infantspant',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='infantspant',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='infantspant',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='kaftan',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='kaftan',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='kaftan',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='kaftan',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='kaftan',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='ladiesblouse',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='ladiesblouse',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='ladiesblouse',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='ladiesblouse',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='ladiesblouse',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='ladiespant',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='ladiespant',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='ladiespant',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='ladiespant',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='ladiespant',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='ladiesskirt',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='ladiesskirt',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='ladiesskirt',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='ladiesskirt',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='ladiesskirt',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='ladiestshirt',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='ladiestshirt',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='ladiestshirt',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='ladiestshirt',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='ladiestshirt',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='maternityfrock',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='maternityfrock',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='maternityfrock',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='maternityfrock',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='maternityfrock',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='nightwear',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='nightwear',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='nightwear',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='nightwear',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='nightwear',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='teenfrock',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='teenfrock',
            name='fabric_name',
        ),
        migrations.RemoveField(
            model_name='teenfrock',
            name='fabric_supplied_date',
        ),
        migrations.RemoveField(
            model_name='teenfrock',
            name='sample_created_date',
        ),
        migrations.RemoveField(
            model_name='teenfrock',
            name='sample_id',
        ),
        migrations.AddField(
            model_name='boyspant',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.boyspant'),
        ),
        migrations.AddField(
            model_name='boysshirt',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.boysshirt'),
        ),
        migrations.AddField(
            model_name='boysshort',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.boysshort'),
        ),
        migrations.AddField(
            model_name='boystshirt',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.boystshirt'),
        ),
        migrations.AddField(
            model_name='girlsfrock',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.girlsfrock'),
        ),
        migrations.AddField(
            model_name='girlspant',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.girlspant'),
        ),
        migrations.AddField(
            model_name='girlsshort',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.girlsshort'),
        ),
        migrations.AddField(
            model_name='girlstshirt',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.girlstshirt'),
        ),
        migrations.AddField(
            model_name='infantsfrock',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.infantsfrock'),
        ),
        migrations.AddField(
            model_name='infantspant',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.infantspant'),
        ),
        migrations.AddField(
            model_name='kaftan',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.kaftan'),
        ),
        migrations.AddField(
            model_name='ladiesblouse',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.ladiesblouse'),
        ),
        migrations.AddField(
            model_name='ladiespant',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.ladiespant'),
        ),
        migrations.AddField(
            model_name='ladiesskirt',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.ladiesskirt'),
        ),
        migrations.AddField(
            model_name='ladiestshirt',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.ladiestshirt'),
        ),
        migrations.AddField(
            model_name='maternityfrock',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.maternityfrock'),
        ),
        migrations.AddField(
            model_name='nightwear',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.nightwear'),
        ),
        migrations.AddField(
            model_name='teenfrock',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sample.teenfrock'),
        ),
        migrations.AlterField(
            model_name='boyspant',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='boysshirt',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='boysshort',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='boystshirt',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='girlsfrock',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='girlspant',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='girlsshort',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='girlstshirt',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='infantsfrock',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='infantspant',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='kaftan',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ladiesblouse',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ladiespant',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ladiesskirt',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ladiestshirt',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='maternityfrock',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nightwear',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teenfrock',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]