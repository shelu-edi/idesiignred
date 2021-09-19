from django import forms
from django.forms import fields, widgets

from .models import Sewing

# forms

class SewingForm(forms.ModelForm):
	order_received = forms.DateField(label='Order Received')
	date_order_delivered = forms.DateField(label='Date Order Delivered')
	style_no = forms.CharField(label='Style No', widget=forms.TextInput(attrs={
		'placeholder': 'Style No'
		}))
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={
		'placeholder': 'Remarks'
		}))
	required_date = forms.DateField(label='Required Date')
	order_accepted = forms.BooleanField(label='Order Accepted')
	order_progress = forms.CharField(label='Order Progress', widget=forms.TextInput(attrs={
		'placeholder': 'Order Progress'
		}))
	completed_date = forms.DateField(label='Completed Date')
	release_date = forms.DateField(label='Release Date')
	reason = forms.CharField(label='Reason', widget=forms.TextInput(attrs={
		'placeholder': 'Reason'
		}))

	class Meta:
		model = Sewing
		fields = [
			'order_received',
			'date_order_delivered',
			'style_no',
			'remarks',
			'required_date',
			'order_accepted',
			'order_progress',
			'completed_date'
			'release_date',
			'reason',
			]
