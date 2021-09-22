from django import forms
from django.forms import fields, widgets

from .models import *
from customers.models import Customer

# forms

# Ladies
class LadiesFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = LadiesFrock
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class LadiesBlouseForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = LadiesBlouse
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]	

class LadiesSkirtForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = LadiesSkirt
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class LadiesPantForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = LadiesPant
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class MaternityFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = MaternityFrock
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class KaftanForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = Kaftan
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]	

class LadiesTshirtForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = LadiesTshirt
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]										

class NightwearForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = Nightwear
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

# Children
class ChildrensFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = ChildrensFrock
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class ChildrensPantForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = ChildrensPant
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]	

#Infant
class InfantsFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = InfantsFrock
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class InfantsPantForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = InfantsPant
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

#Girl 
class GirlsFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = GirlsFrock
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class GirlsPantForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = GirlsPant
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]	

class GirlsTshirtForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = GirlsTshirt
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class GirlsShortForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = GirlsShort
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

#Boys
class BoysPantForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = BoysPant
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class BoysShirtForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = BoysShirt
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class BoysTshirtForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = BoysTshirt
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

class BoysShortForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = BoysShort
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]

#Teens
class TeenfrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manifacture Date')
	sample_id = forms.CharField(label='Sample ID', widget=forms.TextInput(attrs={
		'placeholder': 'Sample ID'
		}))
	sample_created_date = forms.DateField(label='Sample Created Date')
	fabric_name = forms.CharField(label='Fabric Name', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Name'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_supplied_date = forms.DateField(label='Fabric Supplied Date', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Supplied Date'
		}))
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.CharField(label='Approved By', widget=forms.TextInput(attrs={
		'placeholder': 'Approved By'
		}))
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	model = Teenfrock
	fields = [
		'product_name',
		'product_id',
		'product_manufacture_date',
		'sample_id',
		'sample_created_date',
		'fabric_name',
		'fabric_id',
		'fabric_supplied_date',
		'total_quantity',
		'total_price',
		'approved_by',
		'approved_on',
		'notes'
		]																										