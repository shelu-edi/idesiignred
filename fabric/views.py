from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator

from django.views import View

from .models import *
from .forms import *


# Create your views here.


# @user_passes_test(lambda u: u.groups.filter(name='fabric').count() == 0, login_url='/users/login')
@method_decorator(login_required(login_url='../users/login'), name='get')
class FabricMainView(View):
    template_name = 'fabric_main.html'
    order_in_query = OrderIn.objects.all()
    order_out_query = OrderOut.objects.all()

    def get_order_in_query_set(self):
        return self.order_in_query

    def get_order_out_query_set(self):
        return self.order_out_query

    def get(self, request):
        form_order_in = OrderInForm()
        form_order_out = OrderOutForm()
        context = {
            'order_ins': self.get_order_in_query_set(),
            'order_outs': self.get_order_out_query_set(),
            'form_order_in': form_order_in,
            'form_order_out': form_order_out
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form_order_in = OrderInForm(request.POST)
        form_order_out = OrderOutForm(request.POST)

        if form_order_in.is_valid():
            form_order_in.save()
            form_order_in = OrderInForm()

        if form_order_out.is_valid():
            form_order_out.save()
            form_order_out = OrderOutForm()

        context = {
            'form_order_in': form_order_in,
            'form_order_out': form_order_out}

        return render(request, self.template_name, context)
