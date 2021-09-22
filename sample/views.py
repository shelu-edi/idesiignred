from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.
def sample_main_view(request):

	return render(request, 'sample_main.html', {})

class LadiesFrockView(View):
	template_name = 'ladies_frock.html'
	queryset = LadiesFrock.objects.all()

	def get_query_set(self):
		return self.queryset

	def get(self, request):
		context = {
			'ladies_frocks': self.get_query_set()
		}

		return render(request, self.template_name, context)

