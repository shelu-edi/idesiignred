from django import forms
from django.forms import fields, widgets

from .models import *

# forms


# Ladies
class LadiesFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	fabric = forms.ModelChoiceField(queryset=OrderOut.objects.all())
	fabric_price = forms.DecimalField(label='Fabric Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	accessories = forms.ModelChoiceField(queryset=AccSentOut.objects.all())
	acc_cost = forms.DecimalField(label='Accessories Cost')
	sewing_cost = forms.DecimalField(label='Sewing Cost')
	embroidery_cost = forms.DecimalField(label='Embroidery Cost')
	washed_cost = forms.DecimalField(label='Washed Cost')
	paint_cost = forms.DecimalField(label='Paint Cost')
	factory_profit = forms.DecimalField(label='Fabric Profit')
	total_value = forms.DecimalField(label='Total Value')
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
		model = LadiesFrock
		fields = [
			'img',
			'sample_manufactured_date',
			'style_no',
			'fabric',
			'fabric_price',
			'consumption',
			'accessories',
			'acc_cost',
			'sewing_cost',
			'embroidery_cost',
			'washed_cost',
			'paint_cost',
			'factory_profit',
			'total_value',
			'accepted',
			'description'
		]


class LadiesBlouseForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class LadiesSkirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class LadiesPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class MaternityFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class KaftanForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class LadiesTshirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class NightwearForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


#  Childrens
class ChildrensFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class ChildrensPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


# Infants
class InfantsFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class InfantsPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


# Girls
class GirlsFrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class GirlsPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class GirlsTshirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class GirlsShortForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]

# Boys
class BoysPantForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
		]


class BoysShirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class BoysTshirtForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


class BoysShortForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]


# Teens
class TeenfrockForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	sample_manufactured_date = forms.DateField(label='Sample Manufactured Date')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
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
	accepted = forms.BooleanField(label='Accepted', required=False)
	description = forms.CharField(label='Description', widget=forms.TextInput(attrs={
		'placeholder': 'Description'
		}))

	class Meta:
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
			'total_value',
			'accepted',
			'description'
			]
