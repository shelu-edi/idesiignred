from django import forms
from django.forms import fields, widgets

from .models import OrderIn, OrderOut

# forms

class OrderInForm(forms.ModelForm):
	order_received = forms.DateField(label='Order Received')
	date_order_delivered = forms.DateField(label='Date Order Delivered')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={
		'placeholder': 'Remarks'
		}))
	required_date = forms.DateField(label='Required Date')
	price = forms.DecimalField(label='Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	total_consumption = forms.CharField(label='Total Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Total Consumption'
		}))
	delivery_date = forms.DateField(label='Delivery Date')
	order_status = forms.BooleanField(label='TouchScreen')
	order_progress = forms.CharField(label='Order Progress', widget=forms.TextInput(attrs={
		'placeholder': 'Order Progress'
		}))
	reason = forms.CharField(label='Reason', widget=forms.TextInput(attrs={
		'placeholder': 'Reason'
		}))

	class Meta:
		model = OrderIn
		fields = [
			'order_received',
			'date_order_delivered',
			'style_no',
			'remarks',
			'required_date',
			'price',
			'consumption',
			'total_consumption',
			'delivery_date',
			'order_status',
			'order_progress',
			'reason',
			]


class OrderOutForm(forms.ModelForm):
	fabric_id = forms.CharField(label='Fabric ID', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric ID'
		}))
	order_received = forms.DateField(label='Order Received')
	date_order_delivered = forms.DateField(label='Date Order Delivered')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={
		'placeholder': 'Remarks'
		}))
	required_date = forms.DateField(label='Required Date')
	quantity = forms.IntegerField(label='Quantity')
	price = forms.DecimalField(label='Price')
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	total_consumption = forms.CharField(label='Total Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Total Consumption'
		}))
	delivery_date = forms.DateField(label='Delivery Date')
	order_status = forms.BooleanField(label='Order Status')
	order_progress = forms.CharField(label='Order Progress', widget=forms.TextInput(attrs={
		'placeholder': 'Order Progress'
		}))
	reason = forms.CharField(label='Reason', widget=forms.TextInput(attrs={
		'placeholder': 'Reason'
		}))

	class Meta:
		model = OrderOut
		fields = [
			'fabric_id',
			'order_received',
			'date_order_delivered',
			'style_no',
			'remarks',
			'required_date',
			'quantity',
			'price',
			'consumption',
			'total_consumption',
			'delivery_date',
			'order_status',
			'order_progress',
			'reason',
			]			
