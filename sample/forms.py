from django import forms
from django.forms import fields, widgets

from .models import *

# forms

# Ladies
class LadiesFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	#fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
	#	'placeholder': 'Fabric ID'
	#	}))
	fabric = forms.ModelChoiceField(queryset=OrderOut.objects.all())
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	#acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
	#	'placeholder': 'Accessories Name'
	#	}))
	#acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
	#	'placeholder': 'Accessories ID'
	#	}))
	accessories = forms.ModelChoiceField(queryset=AccSentOut.objects.all())
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = LadiesFrock
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		#'fabric_id',
		'fabric',
		'fabric_price',
		'consumption',
		'accessories',
		#'acc_name',
		#'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class LadiesBlouseForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = LadiesBlouse
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]	

class LadiesSkirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = LadiesSkirt
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class LadiesPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = LadiesPant
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class MaternityFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = MaternityFrock
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class KaftanForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = Kaftan
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class LadiesTshirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = LadiesTshirt
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class NightwearForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = Nightwear
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

#Childrens
class ChildrensFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = ChildrensFrock
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class ChildrensPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = ChildrensPant
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

#Infants
class InfantsFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = InfantsFrock
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class InfantsPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = InfantsPant
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

#Girls
class GirlsFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = GirlsFrock
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class GirlsPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = GirlsPant
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class GirlsTshirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = GirlsTshirt
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class GirlsShortForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = GirlsShort
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

#Boys
class BoysPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = BoysPant
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]	

class BoysShirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = BoysShirt
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class BoysTshirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = BoysTshirt
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]

class BoysShortForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = BoysShort
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]	

#Teens
class TeenfrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField('Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder'; 'Style No'
		}))
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted')
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	model = Teenfrock
	fields = [
		'img',
		'sample_manufactured_date',
		'style_no',
		'fabric_id',
		'fabric_price',
		'consumption',
		'acc_name',
		'acc_id',
		'acc_cost',
		'sewing_cost',
		'embroidery_cost',
		'washed_cost',
		'paint_cost',
		'factory_profit',
		'total_price',
		'accepted',
		'description'
		]																																					