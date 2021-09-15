from django import forms
from django.forms import fields, widgets

from .models import AccRecievedIn, AccSentOut

# forms

class AccRecievedInForm(forms.ModelForm):
	date = forms.DateField(label='Date')
	invoice_no = forms.CharField(label='Invoice No', widget=forms.TextInput(attrs={
		'placeholder': 'Invoice No'
		})) # change this once invoice model is completed
	price = forms.DecimalField(label='Price')
	quantity = forms.IntegerField(label='Quantity')
	value = forms.IntegerField(label='value')
	customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={
		'placeholder': 'Customer Name'
		}))
	customer_id = forms.CharField(label='Customer ID', widget=forms.TextInput(attrs={
		'placeholder': 'Customer ID'
		}))
	delivery_date = forms.DateField(label='Delivery Date')
	time = forms.CharField(label='Time', widget=forms.TextInput(attrs={
		'placeholder': 'Time'
		}))
	user_notes = forms.CharField(label='User Notes', widget=forms.TextInput(attrs={
		'placeholder': 'User Notes'
		}))

	class Meta:
		model = AccRecievedIn
		fields = [
			'date',
			'invoice_no',
			'price',
			'quantity',
			'value',
			'customer_name',
			'customer_id',
			'delivery_date',
			'time',
			'user_notes']

class AccSentOutForm(forms.ModelForm):
	date = forms.DateField(label='Date')
	invoice_no = forms.CharField(label='Invoice No', widget=forms.TextInput(attrs={
		'placeholder': 'Invoice No'
		})) # change this once invoice model is completed
	price = forms.DecimalField(label='Price')
	quantity = forms.IntegerField(label='Quantity')
	value = forms.IntegerField(label='value')
	customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={
		'placeholder': 'Customer Name'
		}))
	customer_id = forms.CharField(label='Customer ID', widget=forms.TextInput(attrs={
		'placeholder': 'Customer ID'
		}))
	delivery_date = forms.DateField(label='Delivery Date')
	time = forms.CharField(label='Time', widget=forms.TextInput(attrs={
		'placeholder': 'Time'
		}))
	user_notes = forms.CharField(label='User Notes', widget=forms.TextInput(attrs={
		'placeholder': 'User Notes'
		}))

	class Meta:
		model = AccSentOut
		fields = [
			'date',
			'invoice_no',
			'price',
			'quantity',
			'value',
			'customer_name',
			'customer_id',
			'delivery_date',
			'time',
			'user_notes']			