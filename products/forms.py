from django import forms
from django.forms import fields, widgets

from .models import *
from django.contrib.auth.models import User
from customers.models import Customer
from sample.models import LadiesFrock as LadiesFrockSample, LadiesBlouse as LadiesBlouseSample, LadiesPant as LadiesPantSample, \
	LadiesSkirt as LadiesSkirtSample, LadiesTshirt as LadiesTshirtSample, MaternityFrock as MaternityFrockSample, Kaftan as KaftanSample, \
	Nightwear as NightwearSample, \
	BoysPant as BoysPantSample, BoysShirt as BoysShirtSample, BoysTshirt as BoysTshirtSample, BoysShort as BoysShortSample, \
	GirlsFrock as GirlsFrockSample, GirlsPant as GirlsPantSample, GirlsTshirt as GirlsTshirtSample, GirlsShort as GirlsShortSample, \
	InfantsFrock as InfantsFrockSample, InfantsPant as InfantsPantSample, \
	Teenfrock as TeenfrockSample
from fabric.models import OrderOut

# forms


# Ladies
class LadiesFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=LadiesFrockSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = LadiesFrock
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=LadiesBlouseSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = LadiesBlouse
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=LadiesSkirtSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = LadiesSkirt
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=LadiesPantSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = LadiesPant
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=MaternityFrockSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = MaternityFrock
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=KaftanSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = Kaftan
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=LadiesTshirtSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = LadiesTshirt
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=NightwearSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = Nightwear
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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


# Infant
class InfantsFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=InfantsFrockSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = InfantsFrock
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=InfantsPantSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = InfantsPant
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
			'approved_by',
			'approved_on',
			'notes'
			]


# Girl
class GirlsFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=GirlsFrockSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = GirlsFrock
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=GirlsPantSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = GirlsPant
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=GirlsTshirtSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = GirlsTshirt
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=GirlsShortSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = GirlsShort
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
			'approved_by',
			'approved_on',
			'notes'
			]


# Boys
class BoysPantForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=BoysPantSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = BoysPant
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=BoysShirtSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = BoysShirt
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=BoysTshirtSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = BoysTshirt
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
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
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=BoysShortSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = BoysShort
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
			'approved_by',
			'approved_on',
			'notes'
			]


# Teens
class TeenFrockForm(forms.ModelForm):
	product_name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
		'placeholder': 'Product Name'
		}))
	product_id = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={
		'placeholder': 'Product ID'
		}))
	product_manufacture_date = forms.DateField(label='Product Manufacture Date')
	sample = forms.ModelChoiceField(label='Sample', queryset=TeenfrockSample.objects.all())
	total_quantity = forms.IntegerField(label='Total Quantity')
	total_price = forms.DecimalField(label='Total Price')
	customer = forms.ModelChoiceField(label='Customer', queryset=Customer.objects.all())
	approved_by = forms.ModelChoiceField(label='Approved By', queryset=User.objects.all())
	approved_on = forms.DateField(label='Approved On')
	notes = forms.CharField(label='Notes', widget=forms.TextInput(attrs={
		'placeholder': 'Notes'
		}))

	class Meta:
		model = TeenFrock
		fields = [
			'product_name',
			'product_id',
			'product_manufacture_date',
			'sample',
			'total_quantity',
			'total_price',
			'customer',
			'approved_by',
			'approved_on',
			'notes'
			]

