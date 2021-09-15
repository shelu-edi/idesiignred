from django.shortcuts import render

# Create your views here.
def invoice_main_view(request):

	return render(request, 'invoice_main.html')
