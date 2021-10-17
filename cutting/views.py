from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .models import *

# Create your views here.


@method_decorator(login_required(login_url='../users/login'), name='get')
class CuttingMainView(View):
	template_name = 'cutting_main.html'
	recieved_in_query = RecievedIn.objects.all()
	sent_out_query = SentOut.objects.all()

	def get_recieved_in_query_set(self):
		return self.recieved_in_query

	def get_sent_out_query_set(self):
		return self.sent_out_query

	def get(self, request):
		context = {
			'recieved_ins': self.get_recieved_in_query_set(),
			'sent_outs': self.get_sent_out_query_set()
			}			

		return render(request, self.template_name, context)	


