from django.db import models

from customers.models import Customer
from orders.models import OrderReceiving

# Create your models here.

class RecievedIn(models.Model):
	order_recieved = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	fabric_type = models.CharField(max_length=1000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	time = models.BooleanField()
	user_notes = models.CharField(max_length=10000)

class SentOut(models.Model):
	order_recieved = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	quantity = models.IntegerField()
	fabric_type = models.CharField(max_length=1000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	time = models.BooleanField()
	user_notes = models.CharField(max_length=10000)		
