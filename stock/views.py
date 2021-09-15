from django.shortcuts import render

# Create your views here.
def stock_main_view(request):

	return render(request, 'stock_main.html')
