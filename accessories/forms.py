from django import forms
from django.forms import fields, widgets

from .models import AccRecievedIn, AccSentOut

# forms

class AccRecievedInForm(forms.ModelForm):
	date = forms.DateField(label='Date')
	invoice_no = forms.CharField(label='Invoice No', widget=forms.TextInput(attrs={
		'placeholder': 'Invoice No'
		})) # change this once invoice model is completed