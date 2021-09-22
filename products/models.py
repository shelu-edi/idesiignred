from django.db import models

# Create your models here.

from customers.models import Customer

# Ladies wear
class LadiesFrock(models.Model):
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

class LadiesBlouse(models.Model):	
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

class LadiesSkirt(models.Model):
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

class LadiesPant(models.Model):
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

class MaternityFrock(models.Model):
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

class Kaftan(models.Model):
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

class LadiesTshirt(models.Model):
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

class Nightwear(models.Model):
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

class InfantsPant(models.Model):
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

#Girl products
class GirlsFrock(models.Model):
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

class GirlsPant(models.Model):
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

class GirlsTshirt(models.Model):
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


class GirlsShort(models.Model):
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

# Boys products	
class BoysPant(models.Model):
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

class BoysShirt(models.Model):
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

class BoysTshirt(models.Model):
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

class BoysShort(models.Model):
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

# Teen Products
class Teenfrock(models.Model):
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



