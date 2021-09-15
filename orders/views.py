from django.shortcuts import render

# Create your views here.

def order_main_view(request):

	return render(request, 'order_main.html')
