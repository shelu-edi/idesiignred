from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None

    return formcls(data, prefix=prefix)


@method_decorator(login_required(login_url='../users/login'), name='get')
class CustomerMainView(View):
    template_name = 'customers_main.html'
    customer_queryset = Customer.objects.all()

    def get_customer_queryset(self):
        return self.customer_queryset

    def customer_update(self, request, id):

        try:
            obj = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404

        if request.method == 'POST':
            customer_update_form = CustomerForm(data=request.POST, instance=obj)
            if customer_update_form.is_bound and customer_update_form.is_valid():
                customer_update_form.save()
        else:
            customer_update_form = CustomerForm(instance=obj)

        context = {
            'obj': obj,
            'customer_update_form': customer_update_form,
        }

        return render(request, self.template_name, context)

    def get(self, request):

        customer_form = CustomerForm(prefix='customer-form')

        context = {
            'customers': self.get_customer_queryset(),
            'customer_form': customer_form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        customer_form = _get_form(request, CustomerForm, 'customer-form')

        if customer_form.is_bound and customer_form.is_valid():
            customer_form.save()

        context = {
            'customer_form': customer_form,
        }

        return render(request, self.template_name, context)

