from django.db import models

from django.contrib.auth.models import User
from customers.models import Customer
from sample.models import *
from fabric.models import OrderOut

# Create your models here.


# Ladies wear
class LadiesFrock(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(LadiesFrock, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class LadiesBlouse(models.Model):	
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(LadiesBlouse, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class LadiesSkirt(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(LadiesSkirt, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class LadiesPant(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(LadiesPant, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class MaternityFrock(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(MaternityFrock, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class Kaftan(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(Kaftan, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class LadiesTshirt(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(LadiesTshirt, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class Nightwear(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(Nightwear, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id



# Childrens Wear
class ChildrensFrock(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample_id = models.CharField(max_length=100)
	sample_created_date = models.DateField()
	fabric_name = models.CharField(max_length=1000)
	fabric_id = models.CharField(max_length=100)
	fabric_supplied_date = models.DateField()
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.CharField(max_length=1000) # fix this once the user model is done
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)	

class ChildrensPant(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample_id = models.CharField(max_length=100)
	sample_created_date = models.DateField()
	fabric_name = models.CharField(max_length=1000)
	fabric_id = models.CharField(max_length=100)
	fabric_supplied_date = models.DateField()
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.CharField(max_length=1000) # fix this once the user model is done
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)	


# Infant wear
class InfantsFrock(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(InfantsFrock, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class InfantsPant(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(InfantsPant, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


# Girl products
class GirlsFrock(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(GirlsFrock, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class GirlsPant(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(GirlsPant, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class GirlsTshirt(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(GirlsTshirt, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class GirlsShort(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(GirlsShort, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


# Boys products	
class BoysPant(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(BoysPant, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class BoysShirt(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(BoysShirt, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class BoysTshirt(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(BoysTshirt, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


class BoysShort(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(BoysShort, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id


# Teen Products
class TeenFrock(models.Model):
	product_name = models.CharField(max_length=1000)
	product_id = models.CharField(max_length=100, unique=True)
	product_manufacture_date = models.DateField()
	sample = models.ForeignKey(Teenfrock, on_delete=models.SET_NULL, null=True, blank=True)
	total_quantity = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10000)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	approved_on = models.DateField()
	notes = models.CharField(max_length=1000)

	def __str__(self):
		return self.product_name + '- ' + self.product_id



