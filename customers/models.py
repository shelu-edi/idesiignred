from django.db import models

# Create your models here.

# salutation choices
salutation_choices = (
		('mr', 'Mr'),
		('mrs', 'Mrs'),
		('miss', 'Miss')
		)

# mobile number type
mobile_no_type = (
		('mobile', 'Mobile'),
		('home', 'Home'),
		('work', 'Work')
		)
# email type
email_type = (
		('work', 'Work'),
		('personal', 'Personal'))

class Customer(models.Model):
	customer_id = models.CharField(max_length=100)
	salutation = models.CharField(max_length=10, choices=salutation_choices, default='Mr')
	customer_first_name = models.CharField(max_length=500)
	customer_last_name = models.CharField(max_length=500)
	mobile_no = models.IntegerField()
	mobile_no_type = models.CharField(max_length=10, choices=mobile_no_type, default='Mobile')
	email = models.EmailField(max_length=120)
	email_type = models.CharField(max_length=10, choices=email_type, default='Work')
	address = models.CharField(max_length=1000)

