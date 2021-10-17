from django.shortcuts import render
from django.http import Http404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.


@method_decorator(login_required(login_url='../users/login'), name='get')
class InvoiceMainView(View):
    template_name = 'invoice_main.html'
    queryset = Invoice.objects.all()

    def get_query_set(self):
        return self.queryset

    def get(self, request):
        form = InvoiceForm()

        context = {'invoices': self.get_query_set(),
                   'form': form,
                   }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == 'POST':
            form = InvoiceForm(request.POST)
            if form.is_valid():
                new_invoice = InvoiceForm()
                new_invoice = request.POST.get('date')
                new_invoice = request.POST.get('invoice_no')
                new_invoice = request.POST.get('customer')
                new_invoice = request.POST.get('style_no')
                new_invoice = request.POST.get('order')
                new_invoice = request.POST.get('quantity')
                new_invoice = request.POST.get('price')
                new_invoice = request.POST.get('value')
                new_invoice = request.POST.get('method_of_payment')
                new_invoice.save()
                print(new_invoice)
                # form.save()
                # form = InvoiceForm()

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)


@login_required(login_url='../users/login')
def invoice_view(request, id):
    template_name = 'invoice.html'

    try:
        obj = Invoice.objects.get(id=id)
    except Invoice.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = InvoiceForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = InvoiceForm(instance=obj)

    context = {
        'object': obj,
        'form': form,
    }

    return render(request, template_name, context)


@login_required(login_url='../users/login')
def invoice_print_view(request, id):
    template_name = 'invoice_print.html'

    try:
        obj = Invoice.objects.get(id=id)
    except Invoice.DoesNotExist:
        raise Http404

    context = {
        'object': obj,
    }

    return render(request, template_name, context)

