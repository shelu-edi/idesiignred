from django import forms
from django.forms import fields, widgets

from .models import Invoice

# forms
class InvoiceForm(forms.ModelForm):
	date = models.DateField(label='Date')
	invoice_no = models.CharField(label='Invoice No', widget=forms.TextInput(attrs={
		'placeholder': 'Invoice No'
		}))
	#customer_name = models.CharField(label='Customer Name', widget=forms.TextInput(attrs={
	#	'placeholder': 'Customer Name'
	#	}))
	#customer_id = models.CharField(label='Customer ID', widget=forms.TextInput(attrs={
	#	'placeholder': 'Customer ID'
	#	}))
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	#order_no = forms.CharField(label='Order No', widget=forms.TextInput(attrs={
	#	'placeholder': 'Order No'
	#	}))
	quantity = forms.IntegerField(label='Quantity')
	price = models.DecimalField(label='Price')
	value = models.IntegerField(label='Value')

	class Meta:
		model = Invoice
		fields = [
			'date',
			'invoice_no',
			'customer_first_name',
			'customer_last_name',
			'style_no',
			'order',
			'quantity',
			'price',
			'value',
			'method_of_payment']

