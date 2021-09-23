from django.db import models

from customers.models import Customer
from invoice.models import Invoice

# Create your models here.

class AccRecievedIn(models.Model):
	acc_name = models.CharField(max_length=1000)
	acc_id = models.CharField(max_length=100)
	date = models.DateField()
	invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100000)
	quantity = models.IntegerField()
	value = models.IntegerField()
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	delivery_date = models.DateField()
	time = models.CharField(max_length=1000)
	user_notes = models.CharField(max_length=9000)

class AccSentOut(models.Model):
	acc_name = models.CharField(max_length=1000)
	acc_id = models.CharField(max_length=100)
	date = models.DateField()
	invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100000)
	quantity = models.IntegerField()
	value = models.IntegerField()
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	delivery_date = models.DateField()
	time = models.CharField(max_length=1000)
	user_notes = models.CharField(max_length=9000)


