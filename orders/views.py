from django.shortcuts import render

from django.views import View

from .models import OrderReceiving
from .forms import *
from customers.models import Customer

# Create your views here.


class OrderMainView(View):
	template_name = 'order_main.html'
	queryset = OrderReceiving.objects.all()

	def get_query_set(self):
		return self.queryset

	def get(self, request):
		form = OrderReceivingForm()
		context = {'orders': self.get_query_set(), 'form': form}

		return render(request, self.template_name, context)
		
	def post(self, request):
		form = OrderReceivingForm(request.POST)
		if form.is_valid():
			form.save()
			form = OrderReceivingForm()

		context = {'form': form}
		
		return render(request, self.template_name, context)					
