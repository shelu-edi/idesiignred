from django.shortcuts import render

from django.views import View

from .models import *

# Create your views here.

class InvoiceMainView(View):
	template_name = 'invoice_main.html'
	queryset = Invoice.objects.all()

	def get_query_set(self):
		return self.queryset

	def get(self, request):
		context = {'invoices': self.get_query_set()}

		return render(request, self.template_name, context)		
