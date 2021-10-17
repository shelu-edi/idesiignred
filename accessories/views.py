from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *


@method_decorator(login_required(login_url='../users/login'), name='get')
class AccessoriesMainView(View):
	template_name = 'accessories_main.html'
	acc_recieved_in_query = AccRecievedIn.objects.all()
	acc_sent_out_query = AccSentOut.objects.all()

	def get_recieved_in_query_set(self):
		return self.acc_recieved_in_query

	def get_acc_sent_out_query_set(self):
		return self.acc_sent_out_query

	def get(self, request):
		context = {
			'acc_recieveds': self.get_recieved_in_query_set(),
			'acc_sent_outs': self.get_acc_sent_out_query_set()
			}		

		return render(request, self.template_name, context)	 

