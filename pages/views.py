from django.shortcuts import render
from django.db.models import Q

from accessories.models import *
from customers.models import *
from fabric.models import *
from invoice.models import *
from orders.models import *
from pages.models import *
from sample.models import *
from sewing.models import *
from stock.models import *


# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def search_results(request):
    template_name = 'results.html'

    if request.method == 'POST':
        searched = request.POST['searched']

        accessories_received_ins = AccRecievedIn.objects.filter(Q(acc_name__contains=searched) |
                                                                Q(acc_id__contains=searched) |
                                                                Q(date__contains=searched) |
                                                                Q(invoice__date__contains=searched) |
                                                                Q(invoice__invoice_no__contains=searched) |
                                                                Q(invoice__style_no__contains=searched) |
                                                                Q(invoice__order__order_no__contains=searched) |
                                                                Q(invoice__quantity__contains=searched) |
                                                                Q(invoice__price__contains=searched) |
                                                                Q(invoice__value__contains=searched) |
                                                                Q(invoice__method_of_payment__contains=searched) |
                                                                Q(price__contains=searched) |
                                                                Q(value__contains=searched) |
                                                                Q(customer__customer_id__contains=searched) |
                                                                Q(customer__salutation__contains=searched) |
                                                                Q(customer__customer_first_name__contains=searched) |
                                                                Q(customer__customer_last_name__contains=searched) |
                                                                Q(customer__mobile_no__contains=searched) |
                                                                Q(customer__mobile_no_type__contains=searched) |
                                                                Q(customer__email__contains=searched) |
                                                                Q(customer__email_type__contains=searched) |
                                                                Q(customer__address__contains=searched) |
                                                                Q(delivery_date__contains=searched) |
                                                                Q(time__contains=searched) |
                                                                Q(user_notes__contains=searched))

        accessories_sent_outs = AccSentOut.objects.filter(Q(acc_name__contains=searched) |
                                                          Q(acc_id__contains=searched) |
                                                          Q(date__contains=searched) |
                                                          Q(invoice__date__contains=searched) |
                                                          Q(invoice__invoice_no__contains=searched) |
                                                          Q(invoice__style_no__contains=searched) |
                                                          Q(invoice__order__order_no__contains=searched) |
                                                          Q(invoice__quantity__contains=searched) |
                                                          Q(invoice__price__contains=searched) |
                                                          Q(invoice__value__contains=searched) |
                                                          Q(invoice__method_of_payment__contains=searched) |
                                                          Q(price__contains=searched) |
                                                          Q(value__contains=searched) |
                                                          Q(customer__customer_id__contains=searched) |
                                                          Q(customer__salutation__contains=searched) |
                                                          Q(customer__customer_first_name__contains=searched) |
                                                          Q(customer__customer_last_name__contains=searched) |
                                                          Q(customer__mobile_no__contains=searched) |
                                                          Q(customer__mobile_no_type__contains=searched) |
                                                          Q(customer__email__contains=searched) |
                                                          Q(customer__email_type__contains=searched) |
                                                          Q(customer__address__contains=searched) |
                                                          Q(delivery_date__contains=searched) |
                                                          Q(time__contains=searched) |
                                                          Q(user_notes__contains=searched))

        customers = Customer.objects.filter(Q(customer_id__contains=searched) |
                                            Q(salutation__contains=searched) |
                                            Q(customer_first_name__contains=searched) |
                                            Q(customer_last_name__contains=searched) |
                                            Q(mobile_no__contains=searched) |
                                            Q(mobile_no_type__contains=searched) |
                                            Q(email__contains=searched) |
                                            Q(email_type__contains=searched) |
                                            Q(address__contains=searched))

        fabric_order_ins = OrderIn.objects.filter(Q(order_received__contains=searched) |
                                                  Q(date_order_delivered__contains=searched) |
                                                  Q(order__order_received__contains=searched) |
                                                  Q(order__date_order_delivered__contains=searched) |
                                                  Q(order__style_no__contains=searched) |
                                                  Q(order__order_no__contains=searched) |
                                                  Q(order__remarks__contains=searched) |
                                                  Q(order__required_date__contains=searched) |
                                                  Q(order__price__contains=searched) |
                                                  Q(order__customer__customer_first_name=searched) |
                                                  Q(order__customer__customer_last_name=searched) |
                                                  Q(order__consumption__contains=searched) |
                                                  Q(order__total_consumption__contains=searched) |
                                                  Q(order__delivery_date__contains=searched) |
                                                  Q(order__order_status__contains=searched) |
                                                  Q(order__order_progress__contains=searched) |
                                                  Q(order__reason__contains=searched) |
                                                  Q(remarks__contains=searched) |
                                                  Q(required_date__contains=searched) |
                                                  Q(price__contains=searched) |
                                                  Q(customer__customer_id__contains=searched) |
                                                  Q(customer__salutation__contains=searched) |
                                                  Q(customer__customer_first_name__contains=searched) |
                                                  Q(customer__customer_last_name__contains=searched) |
                                                  Q(customer__mobile_no__contains=searched) |
                                                  Q(customer__mobile_no_type__contains=searched) |
                                                  Q(customer__email__contains=searched) |
                                                  Q(customer__email_type__contains=searched) |
                                                  Q(customer__address__contains=searched) |
                                                  Q(consumption__contains=searched) |
                                                  Q(total_consumption__contains=searched) |
                                                  Q(delivery_date__contains=searched) |
                                                  Q(order_status__contains=searched) |
                                                  Q(order_progress__contains=searched) |
                                                  Q(reason__contains=searched))

        fabric_order_outs = OrderOut.objects.filter(Q(fabric_id__contains=searched) |
                                                    Q(order_received__contains=searched) |
                                                    Q(date_order_delivered__contains=searched) |
                                                    Q(order__order_received__contains=searched) |
                                                    Q(order__date_order_delivered__contains=searched) |
                                                    Q(order__style_no__contains=searched) |
                                                    Q(order__order_no__contains=searched) |
                                                    Q(order__remarks__contains=searched) |
                                                    Q(order__required_date__contains=searched) |
                                                    Q(order__price__contains=searched) |
                                                    Q(order__customer__customer_first_name=searched) |
                                                    Q(order__customer__customer_last_name=searched) |
                                                    Q(order__consumption__contains=searched) |
                                                    Q(order__total_consumption__contains=searched) |
                                                    Q(order__delivery_date__contains=searched) |
                                                    Q(order__order_status__contains=searched) |
                                                    Q(order__order_progress__contains=searched) |
                                                    Q(order__reason__contains=searched) |
                                                    Q(remarks__contains=searched) |
                                                    Q(required_date__contains=searched) |
                                                    Q(quantity__contains=searched) |
                                                    Q(price__contains=searched) |
                                                    Q(customer__customer_id__contains=searched) |
                                                    Q(customer__salutation__contains=searched) |
                                                    Q(customer__customer_first_name__contains=searched) |
                                                    Q(customer__customer_last_name__contains=searched) |
                                                    Q(customer__mobile_no__contains=searched) |
                                                    Q(customer__mobile_no_type__contains=searched) |
                                                    Q(customer__email__contains=searched) |
                                                    Q(customer__email_type__contains=searched) |
                                                    Q(customer__address__contains=searched) |
                                                    Q(consumption__contains=searched) |
                                                    Q(total_consumption__contains=searched) |
                                                    Q(delivery_date__contains=searched) |
                                                    Q(order_status__contains=searched) |
                                                    Q(order_progress__contains=searched) |
                                                    Q(reason__contains=searched))

        invoices = Invoice.objects.filter(Q(date__contains=searched) |
                                          Q(invoice_no__contains=searched) |
                                          Q(customer__customer_id__contains=searched) |
                                          Q(customer__salutation__contains=searched) |
                                          Q(customer__customer_first_name__contains=searched) |
                                          Q(customer__customer_last_name__contains=searched) |
                                          Q(customer__mobile_no__contains=searched) |
                                          Q(customer__mobile_no_type__contains=searched) |
                                          Q(customer__email__contains=searched) |
                                          Q(customer__email_type__contains=searched) |
                                          Q(customer__address__contains=searched) |
                                          Q(style_no__contains=searched) |
                                          Q(order__order_received__contains=searched) |
                                          Q(order__date_order_delivered__contains=searched) |
                                          Q(order__style_no__contains=searched) |
                                          Q(order__order_no__contains=searched) |
                                          Q(order__remarks__contains=searched) |
                                          Q(order__required_date__contains=searched) |
                                          Q(order__price__contains=searched) |
                                          Q(order__customer__customer_first_name=searched) |
                                          Q(order__customer__customer_last_name=searched) |
                                          Q(order__consumption__contains=searched) |
                                          Q(order__total_consumption__contains=searched) |
                                          Q(order__delivery_date__contains=searched) |
                                          Q(order__order_status__contains=searched) |
                                          Q(order__order_progress__contains=searched) |
                                          Q(order__reason__contains=searched) |
                                          Q(quantity__contains=searched) |
                                          Q(price__contains=searched) |
                                          Q(value__contains=searched) |
                                          Q(method_of_payment__contains=searched)
                                          )

    context = {
        'searched': searched,
        'customers': customers,
        'accessories_received_ins': accessories_received_ins,
        'accessories_sent_outs': accessories_sent_outs,
        'fabric_order_ins': fabric_order_ins,
        'fabric_order_outs': fabric_order_outs,
        'invoices': invoices,
    }

    return render(request, template_name, context)
