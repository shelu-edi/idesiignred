from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from orders.models import *
from orders.forms import *

# Create your views here.


def stock_main_view(request):
    template_name = 'stock_main.html'

    return render(request, template_name, {})


def stock_create_view(request):
    data = dict()

    if request.method == 'POST':
        form = OrderReceivingForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            orders = OrderReceiving.objects.all()
            data['orders_list'] = render_to_string('stock_list.html', {
                'orders': orders,
            })
        else:
            data['form_is_valid'] = False
    else:
        form = OrderReceivingForm()

    context = {
        'form': form,
    }

    data['html_form'] = render_to_string('stock_create.html', context, request=request)

    return JsonResponse(data)


def stock_update_view(request):
    pass

