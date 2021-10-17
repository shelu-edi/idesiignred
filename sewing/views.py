from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


@method_decorator(login_required(login_url='../users/login'), name='get')
class SewingMainView(View):	
	template_name = 'sewing_main.html'
	queryset = Sewing.objects.all()

	def get_query_set(self):
		return self.queryset

	def get(self, request):
		context = {'sewings': self.get_query_set()}

		return render(request, self.template_name, context)