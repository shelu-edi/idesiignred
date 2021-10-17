from django import forms
from django.forms import fields, widgets

from customers.models import Customer
from orders.models import OrderReceiving
from .models import Invoice


# forms
class InvoiceForm(forms.ModelForm):
	payment_options = (
		("Cash", "Cash"),
		("Check", "Check")
	)

	date = forms.DateField(label='Date')
	invoice_no = forms.CharField(label='Invoice No', widget=forms.TextInput(attrs={
		'placeholder': 'Invoice No'
		}))
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	order = forms.ModelChoiceField(queryset=OrderReceiving.objects.all(), label='Order')
	quantity = forms.IntegerField(label='Quantity')
	price = forms.DecimalField(label='Unit Price')
	value = forms.IntegerField(label='Total Value')
	method_of_payment = forms.MultipleChoiceField(widget=forms.Select, choices=payment_options)

	class Meta:
		model = Invoice
		fields = [
			'date',
			'invoice_no',
			'style_no',
			'order',
			'quantity',
			'price',
			'value',
			'method_of_payment']

