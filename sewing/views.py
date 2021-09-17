from django.shortcuts import render

from django.views import View

from .models import *

# Create your views here.

class SewingMainView(View):	
	template_name = 'sewing_main.html'
	queryset = Sewing.objects.all()

	def get_query_set(self):
		return self.queryset

	def get(self, request):
		context = {'sewings': self.get_query_set()}

		return render(request, self.template_name, context)