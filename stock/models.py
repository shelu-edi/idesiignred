from django.db import models

from customers.models import Customer
from orders.models import OrderReceiving
from sample.models import *

# Create your models here.
class Stock(models.Model):
	stock_date = models.DateField()
	sample = models.ForeignKey(LadiesFrock, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	delivery_date = models.DateField()
	order_delivered = models.BooleanField(default=False)
	quantity = models.IntegerField()
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	accepted = models.BooleanField(default=False)
	received_date = models.DateField()
	damaged = models.BooleanField(default=False)
	remarks = models.CharField(max_length=1000)
	balance_quantity = models.IntegerField()
	completed_date = models.DateField()
	delivered_by = models.CharField(max_length=1000)
	release_date = models.DateField()

	def __str__(self):
		return self.quantity + '- ' + self.date


