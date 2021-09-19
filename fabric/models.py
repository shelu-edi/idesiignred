from django.db import models

from customers.models import Customer
from orders.models import OrderReceiving

# Create your models here.



class OrderIn(models.Model):
	order_received = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
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
	order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	quantity = models.IntegerField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	order_status = models.BooleanField(default=False)
	order_progress = models.CharField(max_length=1000)
	reason = models.CharField(max_length=1000)

