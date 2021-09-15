from django.db import models

# Create your models here.

class OrderIn(models.Model):
	order_received = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order_no = models.CharField(max_length=1000)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	customer_name = models.CharField(max_length=1000)
	customer_id = models.CharField(max_length=1000)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	order_status = models.BooleanField(default=False)
	order_progress = models.CharField(max_length=1000)
	reason = models.CharField(max_length=1000)

class OrderOut(models.Model):
	order_received = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order_no = models.CharField(max_length=1000)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	quantity = models.IntegerField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	customer_name = models.CharField(max_length=1000)
	customer_id = models.CharField(max_length=1000)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	order_status = models.BooleanField(default=False)
	order_progress = models.CharField(max_length=1000)
	reason = models.CharField(max_length=1000)

