from django.db import models

# Create your models here.

class AccRecievedIn(models.Model):
	date = models.DateField()
	invoice_no = models.CharField(max_length=1000)  # make a foreign key once invoice model is completed
	price = models.DecimalField(decimal_places=2, max_digits=100000)
	quantity = models.IntegerField()
	vale = models.IntegerField()
	customer_name = models.CharField(max_length=1000)
	customer_id = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	time = models.CharField(max_length=1000)
	user_notes = models.CharField(max_length=9000)

class AccSentOut(models.Model):
	date = models.DateField()
	invoice_no = models.CharField(max_length=1000)  # make a foreign key once invoice model is completed
	price = models.DecimalField(decimal_places=2, max_digits=100000)
	quantity = models.IntegerField()
	vale = models.IntegerField()
	customer_name = models.CharField(max_length=1000)
	customer_id = models.CharField(max_length=1000)
	delivery_date = models.DateField()
	time = models.CharField(max_length=1000)
	user_notes = models.CharField(max_length=9000)


