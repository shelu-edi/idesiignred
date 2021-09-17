from django.db import models

# Create your models here.

class RecievedIn(models.Model):
	order_recieved = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order_no = models.CharField(max_length=1000)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	fabric_type = models.CharField(max_length=1000)
	customer_name = models.CharField(max_length=1000)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	time = models.BooleanField()
	user_notes = models.CharField(max_length=10000)

class SentOut(models.Model):
	order_recieved = models.DateField()
	date_order_delivered = models.DateField()
	style_no = models.CharField(max_length=1000)
	order_no = models.CharField(max_length=1000)
	remarks = models.CharField(max_length=9000)
	required_date = models.DateField()
	quantity = models.IntegerField()
	fabric_type = models.CharField(max_length=1000)
	customer_name = models.CharField(max_length=1000)
	consumption = models.CharField(max_length=1000)
	total_consumption = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	time = models.BooleanField()
	user_notes = models.CharField(max_length=10000)		
