from django.db import models

from orders.models import OrderReceiving

# Create your models here.

class Sewing(models.Model):
	order_received = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	order_accepted = models.BooleanField(default=False)	
	order_progress = models.CharField(max_length=1000)
	completed_date = models.DateField()
	release_date = models.DateField()
	reason = models.CharField(max_length=1000)
