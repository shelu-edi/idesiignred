from django.db import models

from customers.models import Customer

# Create your models here.

class OrderReceiving(models.Model):
	order_received = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order_no = models.CharField(max_length=1000, unique=True)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	order_status = models.BooleanField(default=False)
	order_progress = models.CharField(max_length=1000)
	reason = models.CharField(max_length=1000)

	def __str__(self):
		return self.order_no + '- ' + self.customer.customer_first_name +  ' ' + self.customer.customer_last_name


