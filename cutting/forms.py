from django import forms
from django.forms import fields, widgets

from .models import RecievedIn, SentOut

# forms

class RecievedInForm(forms.ModelForm):
	order_received = forms.DateField(label='Order Received')
	date_order_delivered = forms.DateField(label='Date Order Delivered')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={
		'placeholder': 'Remarks'
		}))
	required_date = forms.DateField(label='Required Date')
	fabric_type = forms.CharField(label='Fabric Type', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Type'
		}))
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	total_consumption = forms.CharField(label='Total Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Total Consumption'
		}))
	delivery_date = forms.DateField(label='Delivery Date')
	time = forms.BooleanField(default=False)
	user_notes = forms.CharField(label='User Notes', widget=forms.TextInput(attrs={
		'placeholder': 'User Notes'
		}))

	class Meta:
		model = RecievedIn
		fields = [
			'order_received',
			'date_order_delivered',
			'style_no',
			'remarks',
			'required_date',
			'fabric_type',
			'consumption',
			'total_consumption',
			'delivery_date',
			'time',
			'user_notes'
			]

class SentOutForm(forms.ModelForm):
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
	fabric_type = forms.CharField(label='Fabric Type', widget=forms.TextInput(attrs={
		'placeholder': 'Fabric Type'
		}))
	consumption = forms.CharField(label='Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Consumption'
		}))
	total_consumption = forms.CharField(label='Total Consumption', widget=forms.TextInput(attrs={
		'placeholder': 'Total Consumption'
		}))
	delivery_date = forms.DateField(label='Delivery Date')
	time = forms.BooleanField(default=False)
	user_notes = forms.CharField(label='User Notes', widget=forms.TextInput(attrs={
		'placeholder': 'User Notes'
		}))

	class Meta:
		model = SentOut
		fields = [
			'order_received',
			'date_order_delivered',
			'style_no',
			'remarks',
			'required_date',
			'Quantity',
			'fabric_type',
			'consumption',
			'total_consumption',
			'delivery_date',
			'time',
			'user_notes'
			]			
