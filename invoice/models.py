from django.db import models

# Create your models here.

# payment choices
payment_choices = (
		('cash', 'Cash'),
		('check', 'Check'),
		)

class Invoice(models.Model):
	date = models.DateField()
	invoice_no = models.CharField(max_length=1000)
	customer_name = models.CharField(max_length=1000)
	customer_id = models.CharField(max_length=1000)
	style_no = models.CharField(max_length=1000)
	order_no = models.CharField(max_length=1000)
	quantity = models.IntegerField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	value = models.IntegerField()
	method_of_payment = models.CharField(max_length=100, choices=payment_choices, default='Cash')
