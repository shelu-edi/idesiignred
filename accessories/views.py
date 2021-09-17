from django.shortcuts import render

from django.views import View

from .models import *

# Create your views here.
def accessories_main_view(request):
	
	return render(request, 'accessories_main.html')

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

