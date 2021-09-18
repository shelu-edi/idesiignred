from django import forms
from django.forms import fields, widgets

from .models import Customer

# forms
class CustomerForm(forms.ModelForm):
	customer_id = models.CharField(label='Customer ID', widget=forms.TextInput(attrs={
		'placeholder': 'Customer ID'
		}))
	customer_first_name = models.CharField(label='Customer First Name', widget=forms.TextInput(attrs={
		'placeholder': 'Customer First Name'
		}))
	customer_last_name = models.CharField(label='Customer Last Name', widget=forms.TextInput(attrs={
		'placeholder': 'Customer Last Name'
		}))	
	mobile_no = models.IntegerField(label='Mobile Number')
	email = models.EmailField(label='Email', widget=forms.TextInput(attrs={
		'placeholder': 'Email'
		}))
	address = models.CharField(label='Address', widget=forms.TextInput(attrs={
		'placeholder': 'Address'
		}))

	class Meta:
		model = Customer
		fields = [
			'customer_id',
			'salutaion',
			'customer_first_name',
			'customer_last_name',
			'mobile_no',
			'mobile_no_type',
			'email',
			'email_type',
			'address'
			]
