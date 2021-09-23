from django import forms
from django.forms import fields, widgets

from .models import AccRecievedIn, AccSentOut

# forms

class AccRecievedInForm(forms.ModelForm):
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID'. widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	date = forms.DateField(label='Date')
	price = forms.DecimalField(label='Price')
	quantity = forms.IntegerField(label='Quantity')
	value = forms.IntegerField(label='value')
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
			'acc_name',
			'acc_id'
			'date',
			'price',
			'quantity',
			'value',
			'delivery_date',
			'time',
			'user_notes']

class AccSentOutForm(forms.ModelForm):
	acc_name = forms.CharField(label='Accessories Name', widget=forms.TextInput(attrs={
		'placeholder': 'Accessories Name'
		}))
	acc_id = forms.CharField(label='Accessories ID'. widget=forms.TextInput(attrs={
		'placeholder': 'Accessories ID'
		}))
	date = forms.DateField(label='Date')
	price = forms.DecimalField(label='Price')
	quantity = forms.IntegerField(label='Quantity')
	value = forms.IntegerField(label='value')
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
			'acc_name',
			'acc_id'
			'date',
			'price',
			'quantity',
			'value',
			'delivery_date',
			'time',
			'user_notes']			