from django import forms
from django.forms import fields, widgets

from .models import *
from customers.models import Customer
from orders.models import OrderReceiving
from sample.models import *

# forms
class StockForm(forms.ModelForm):
	stock_date = forms.DateField(label='Date')
	sample = forms.ModelChoiceField(queryset=Ladiesfrock.objects.all())
	order = forms.ModelChoiceField(queryset=OrderReceiving.objects.all())
	delivery_date = forms.DateField(label='Delivery Date')
	order_delivered = forms.BooleanField(label='Order Delivered')
	quantity = forms.IntegerField(label='Quantity')
	customer = forms.ModelChoiceField(queryset=Customer.objects.all())	
	accepted = forms.BooleanField(label='Accepted')
	received_date = forms.DateField(label='Recieved Date')
	damaged = forms.BooleanField(label='Damaged')
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={
		'placeholder': 'Remarks'
		}))
	balance_quantity = forms.IntegerField(label='Balance Quantity')
	completed_date = forms.DateField(label='Completed Date')
	delivered_by = forms.CharField(label='Delivered By', widget=forms.TextInput(attrs={
		'placeholder': 'Delivered By'
		}))
	release_date = forms.DateField(label='Release Date')

	model = Stock
	fields = [
		'stock_date',
		'sample',
		'order',
		'delivery_date',
		'order_delivered',
		'quantity',
		'customer',
		'accepted',
		'received_date',
		'damaged',
		'remarks',
		'balance_quantity',
		'completed_date',
		'delivery_date',
		'release_date'
		]
