from django.db import models

from customers.models import Customer
from orders.models import OrderReceiving

# Create your models here.

# payment choices
payment_choices = (
		('cash', 'Cash'),
		('check', 'Check'),
		)

class Invoice(models.Model):
	date = models.DateField()
	invoice_no = models.CharField(max_length=1000, unique=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	#customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	style_no = models.CharField(max_length=1000)
	order =  models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	value = models.IntegerField()
	method_of_payment = models.CharField(max_length=100, choices=payment_choices, default='Cash')

	def __str__(self):
		return self.invoice_no +  '- ' + self.customer.customer_first_name +  ' ' + self.customer.customer_last_name
