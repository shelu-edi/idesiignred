from django import forms
from django.forms import fields, widgets

from .models import OrderReceiving
from customers.models import Customer

# forms

class OrderReceivingForm(forms.ModelForm):
	order_received = forms.DateField(label='Order Received')
	date_order_delivered = forms.DateField(label='Date Order Delivered')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	order_no = forms.CharField(label='Order No', widget=forms.TextInput(attrs={
		'placeholder': 'Order No'
		}))
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={
		'placeholder': 'Remarks'
		}))
	required_date = forms.DateField(label='Required Date')
	price = forms.DecimalField(label='Price')
	#customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={
	#	'placeholder': 'Customer Name'
	#	}))
	#customer_id = forms.CharField(label='Customer ID', widget=forms.TextInput(attrs={
	#	'placeholder': 'Customer ID'
	#	}))
	customer = forms.ModelChoiceField(queryset=Customer.objects.all())
	#customer_last_name = forms.ModelChoiceField(queryset=Customer.objects.all())
	#customer_id = forms.ModelChoiceField(queryset=Customer.objects.all())
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
		model = OrderReceiving
		fields = [
			'order_received',
			'date_order_delivered',
			'style_no',
			'order_no',
			'remarks',
			'required_date',
			'price',
			'customer',
			'consumption',
			'total_consumption',
			'delivery_date',
			'order_status',
			'order_progress',
			'reason',
			]
