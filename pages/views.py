from django.shortcuts import render
from django.db.models import Q

from accessories.models import *
from customers.models import *
from fabric.models import *
from invoice.models import *
from orders.models import *
from sample.models import *
from sewing.models import *
from stock.models import *
from products.models import LadiesFrock as LadiesFrockProduct, LadiesSkirt as LadiesSkirtProduct, \
    LadiesBlouse as LadiesBlouseProduct, LadiesTshirt as LadiesTshirtProduct, \
    MaternityFrock as MaternityFrockProduct, Kaftan as KaftanProduct, Nightwear as NightwearProduct, \
    BoysPant as BoysPantProduct, BoysShirt as BoysShirtProduct, BoysTshirt as BoysTshirtProduct, \
    BoysShort as BoysShortProduct, \
    GirlsFrock as GirlsFrockProduct, GirlsPant as GirlsPantProduct, GirlsTshirt as GirlsTshirtProduct, \
    GirlsShort as GirlsShortproduct, \
    InfantsFrock as InfantsFrockProduct, InfantsPant as InfantsPantProduct, \
    Teenfrock as TeensFrockProduct


# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def search_results(request):
    template_name = 'results.html'

    if request.method == 'POST':
        searched = request.POST['searched']

        # accessories
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

        # fabric
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

        # invoice
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
        # order
        order_receivings = OrderReceiving.objects.filter(Q(order_received__contains=searched) |
                                                         Q(date_order_delivered__contains=searched) |
                                                         Q(style_no__contains=searched) |
                                                         Q(order_no__contains=searched) |
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
                                                         Q(reason__contains=searched)
                                                         )

        # sample
        # ladies
        ladies_frocks = LadiesFrock.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                   Q(style_no__contains=searched) |
                                                   Q(fabric__fabric_id__contains=searched) |
                                                   Q(fabric__order_received__contains=searched) |
                                                   Q(fabric__date_order_delivered__contains=searched) |
                                                   Q(fabric__style_no__contains=searched) |
                                                   Q(fabric__order__order_no=searched) |
                                                   Q(fabric__remarks__contains=searched) |
                                                   Q(fabric__required_date__contains=searched) |
                                                   Q(fabric__quantity__contains=searched) |
                                                   Q(fabric__price__contains=searched) |
                                                   Q(fabric__customer__customer_first_name__contains=searched) |
                                                   Q(fabric__customer__customer_last_name__contains=searched) |
                                                   Q(fabric__consumption__contains=searched) |
                                                   Q(fabric__total_consumption__contains=searched) |
                                                   Q(fabric__delivery_date__contains=searched) |
                                                   Q(fabric__order_status__contains=searched) |
                                                   Q(fabric__order_progress__contains=searched) |
                                                   Q(fabric__reason__contains=searched) |
                                                   Q(fabric_price__contains=searched) |
                                                   Q(consumption__contains=searched) |
                                                   Q(acc_name__contains=searched) |
                                                   Q(accessories__acc_name__contains=searched) |
                                                   Q(accessories__acc_id__contains=searched) |
                                                   Q(accessories__date__contains=searched) |
                                                   Q(accessories__invoice__invoice_no__contains=searched) |
                                                   Q(accessories__price__contains=searched) |
                                                   Q(accessories__quantity__contains=searched) |
                                                   Q(accessories__value__contains=searched) |
                                                   Q(accessories__customer__customer_first_name__contains=searched) |
                                                   Q(accessories__customer__customer_last_name__contains=searched) |
                                                   Q(accessories__delivery_date__contains=searched) |
                                                   Q(accessories__time__contains=searched) |
                                                   Q(accessories__user_notes__contains=searched) |
                                                   Q(acc_cost__contains=searched) |
                                                   Q(sewing_cost__contains=searched) |
                                                   Q(embroidery_cost__contains=searched) |
                                                   Q(washed_cost__contains=searched) |
                                                   Q(paint_cost__contains=searched) |
                                                   Q(factory_profit__contains=searched) |
                                                   Q(total_value__contains=searched) |
                                                   Q(accepted__contains=searched) |
                                                   Q(description__contains=searched)
                                                   )

        ladies_blouses = LadiesBlouse.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                     Q(style_no__contains=searched) |
                                                     Q(fabric_id__contains=searched) |
                                                     Q(fabric_price__contains=searched) |
                                                     Q(consumption__contains=searched) |
                                                     Q(acc_name__contains=searched) |
                                                     Q(acc_id__contains=searched) |
                                                     Q(acc_cost__contains=searched) |
                                                     Q(sewing_cost__contains=searched) |
                                                     Q(embroidery_cost__contains=searched) |
                                                     Q(washed_cost__contains=searched) |
                                                     Q(paint_cost__contains=searched) |
                                                     Q(factory_profit__contains=searched) |
                                                     Q(total_value__contains=searched) |
                                                     Q(accepted__contains=searched) |
                                                     Q(description__contains=searched)
                                                     )

        ladies_skirts = LadiesSkirt.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                   Q(style_no__contains=searched) |
                                                   Q(fabric_id__contains=searched) |
                                                   Q(fabric_price__contains=searched) |
                                                   Q(consumption__contains=searched) |
                                                   Q(acc_name__contains=searched) |
                                                   Q(acc_id__contains=searched) |
                                                   Q(acc_cost__contains=searched) |
                                                   Q(sewing_cost__contains=searched) |
                                                   Q(embroidery_cost__contains=searched) |
                                                   Q(washed_cost__contains=searched) |
                                                   Q(paint_cost__contains=searched) |
                                                   Q(factory_profit__contains=searched) |
                                                   Q(total_value__contains=searched) |
                                                   Q(accepted__contains=searched) |
                                                   Q(description__contains=searched)
                                                   )

        ladies_pants = LadiesPant.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                 Q(style_no__contains=searched) |
                                                 Q(fabric_id__contains=searched) |
                                                 Q(fabric_price__contains=searched) |
                                                 Q(consumption__contains=searched) |
                                                 Q(acc_name__contains=searched) |
                                                 Q(acc_id__contains=searched) |
                                                 Q(acc_cost__contains=searched) |
                                                 Q(sewing_cost__contains=searched) |
                                                 Q(embroidery_cost__contains=searched) |
                                                 Q(washed_cost__contains=searched) |
                                                 Q(paint_cost__contains=searched) |
                                                 Q(factory_profit__contains=searched) |
                                                 Q(total_value__contains=searched) |
                                                 Q(accepted__contains=searched) |
                                                 Q(description__contains=searched)
                                                 )

        maternity_frocks = MaternityFrock.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                         Q(style_no__contains=searched) |
                                                         Q(fabric_id__contains=searched) |
                                                         Q(fabric_price__contains=searched) |
                                                         Q(consumption__contains=searched) |
                                                         Q(acc_name__contains=searched) |
                                                         Q(acc_id__contains=searched) |
                                                         Q(acc_cost__contains=searched) |
                                                         Q(sewing_cost__contains=searched) |
                                                         Q(embroidery_cost__contains=searched) |
                                                         Q(washed_cost__contains=searched) |
                                                         Q(paint_cost__contains=searched) |
                                                         Q(factory_profit__contains=searched) |
                                                         Q(total_value__contains=searched) |
                                                         Q(accepted__contains=searched) |
                                                         Q(description__contains=searched)
                                                         )

        kaftans = Kaftan.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                        Q(style_no__contains=searched) |
                                        Q(fabric_id__contains=searched) |
                                        Q(fabric_price__contains=searched) |
                                        Q(consumption__contains=searched) |
                                        Q(acc_name__contains=searched) |
                                        Q(acc_id__contains=searched) |
                                        Q(acc_cost__contains=searched) |
                                        Q(sewing_cost__contains=searched) |
                                        Q(embroidery_cost__contains=searched) |
                                        Q(washed_cost__contains=searched) |
                                        Q(paint_cost__contains=searched) |
                                        Q(factory_profit__contains=searched) |
                                        Q(total_value__contains=searched) |
                                        Q(accepted__contains=searched) |
                                        Q(description__contains=searched)
                                        )

        ladies_tshirts = LadiesTshirt.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                     Q(style_no__contains=searched) |
                                                     Q(fabric_id__contains=searched) |
                                                     Q(fabric_price__contains=searched) |
                                                     Q(consumption__contains=searched) |
                                                     Q(acc_name__contains=searched) |
                                                     Q(acc_id__contains=searched) |
                                                     Q(acc_cost__contains=searched) |
                                                     Q(sewing_cost__contains=searched) |
                                                     Q(embroidery_cost__contains=searched) |
                                                     Q(washed_cost__contains=searched) |
                                                     Q(paint_cost__contains=searched) |
                                                     Q(factory_profit__contains=searched) |
                                                     Q(total_value__contains=searched) |
                                                     Q(accepted__contains=searched) |
                                                     Q(description__contains=searched)
                                                     )

        nightwears = Nightwear.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                              Q(style_no__contains=searched) |
                                              Q(fabric_id__contains=searched) |
                                              Q(fabric_price__contains=searched) |
                                              Q(consumption__contains=searched) |
                                              Q(acc_name__contains=searched) |
                                              Q(acc_id__contains=searched) |
                                              Q(acc_cost__contains=searched) |
                                              Q(sewing_cost__contains=searched) |
                                              Q(embroidery_cost__contains=searched) |
                                              Q(washed_cost__contains=searched) |
                                              Q(paint_cost__contains=searched) |
                                              Q(factory_profit__contains=searched) |
                                              Q(total_value__contains=searched) |
                                              Q(accepted__contains=searched) |
                                              Q(description__contains=searched)
                                              )

        # boys
        boys_pants = BoysPant.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                             Q(style_no__contains=searched) |
                                             Q(fabric_id__contains=searched) |
                                             Q(fabric_price__contains=searched) |
                                             Q(consumption__contains=searched) |
                                             Q(acc_name__contains=searched) |
                                             Q(acc_id__contains=searched) |
                                             Q(acc_cost__contains=searched) |
                                             Q(sewing_cost__contains=searched) |
                                             Q(embroidery_cost__contains=searched) |
                                             Q(washed_cost__contains=searched) |
                                             Q(paint_cost__contains=searched) |
                                             Q(factory_profit__contains=searched) |
                                             Q(total_value__contains=searched) |
                                             Q(accepted__contains=searched) |
                                             Q(description__contains=searched)
                                             )

        boys_shirts = BoysShirt.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                               Q(style_no__contains=searched) |
                                               Q(fabric_id__contains=searched) |
                                               Q(fabric_price__contains=searched) |
                                               Q(consumption__contains=searched) |
                                               Q(acc_name__contains=searched) |
                                               Q(acc_id__contains=searched) |
                                               Q(acc_cost__contains=searched) |
                                               Q(sewing_cost__contains=searched) |
                                               Q(embroidery_cost__contains=searched) |
                                               Q(washed_cost__contains=searched) |
                                               Q(paint_cost__contains=searched) |
                                               Q(factory_profit__contains=searched) |
                                               Q(total_value__contains=searched) |
                                               Q(accepted__contains=searched) |
                                               Q(description__contains=searched)
                                               )

        boys_tshirts = BoysTshirt.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                 Q(style_no__contains=searched) |
                                                 Q(fabric_id__contains=searched) |
                                                 Q(fabric_price__contains=searched) |
                                                 Q(consumption__contains=searched) |
                                                 Q(acc_name__contains=searched) |
                                                 Q(acc_id__contains=searched) |
                                                 Q(acc_cost__contains=searched) |
                                                 Q(sewing_cost__contains=searched) |
                                                 Q(embroidery_cost__contains=searched) |
                                                 Q(washed_cost__contains=searched) |
                                                 Q(paint_cost__contains=searched) |
                                                 Q(factory_profit__contains=searched) |
                                                 Q(total_value__contains=searched) |
                                                 Q(accepted__contains=searched) |
                                                 Q(description__contains=searched)
                                                 )

        boys_shorts = BoysShort.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                               Q(style_no__contains=searched) |
                                               Q(fabric_id__contains=searched) |
                                               Q(fabric_price__contains=searched) |
                                               Q(consumption__contains=searched) |
                                               Q(acc_name__contains=searched) |
                                               Q(acc_id__contains=searched) |
                                               Q(acc_cost__contains=searched) |
                                               Q(sewing_cost__contains=searched) |
                                               Q(embroidery_cost__contains=searched) |
                                               Q(washed_cost__contains=searched) |
                                               Q(paint_cost__contains=searched) |
                                               Q(factory_profit__contains=searched) |
                                               Q(total_value__contains=searched) |
                                               Q(accepted__contains=searched) |
                                               Q(description__contains=searched)
                                               )

        # girls
        girls_frocks = GirlsFrock.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                 Q(style_no__contains=searched) |
                                                 Q(fabric_id__contains=searched) |
                                                 Q(fabric_price__contains=searched) |
                                                 Q(consumption__contains=searched) |
                                                 Q(acc_name__contains=searched) |
                                                 Q(acc_id__contains=searched) |
                                                 Q(acc_cost__contains=searched) |
                                                 Q(sewing_cost__contains=searched) |
                                                 Q(embroidery_cost__contains=searched) |
                                                 Q(washed_cost__contains=searched) |
                                                 Q(paint_cost__contains=searched) |
                                                 Q(factory_profit__contains=searched) |
                                                 Q(total_value__contains=searched) |
                                                 Q(accepted__contains=searched) |
                                                 Q(description__contains=searched)
                                                 )

        girls_pants = GirlsPant.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                               Q(style_no__contains=searched) |
                                               Q(fabric_id__contains=searched) |
                                               Q(fabric_price__contains=searched) |
                                               Q(consumption__contains=searched) |
                                               Q(acc_name__contains=searched) |
                                               Q(acc_id__contains=searched) |
                                               Q(acc_cost__contains=searched) |
                                               Q(sewing_cost__contains=searched) |
                                               Q(embroidery_cost__contains=searched) |
                                               Q(washed_cost__contains=searched) |
                                               Q(paint_cost__contains=searched) |
                                               Q(factory_profit__contains=searched) |
                                               Q(total_value__contains=searched) |
                                               Q(accepted__contains=searched) |
                                               Q(description__contains=searched)
                                               )

        girls_tshirts = GirlsTshirt.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                   Q(style_no__contains=searched) |
                                                   Q(fabric_id__contains=searched) |
                                                   Q(fabric_price__contains=searched) |
                                                   Q(consumption__contains=searched) |
                                                   Q(acc_name__contains=searched) |
                                                   Q(acc_id__contains=searched) |
                                                   Q(acc_cost__contains=searched) |
                                                   Q(sewing_cost__contains=searched) |
                                                   Q(embroidery_cost__contains=searched) |
                                                   Q(washed_cost__contains=searched) |
                                                   Q(paint_cost__contains=searched) |
                                                   Q(factory_profit__contains=searched) |
                                                   Q(total_value__contains=searched) |
                                                   Q(accepted__contains=searched) |
                                                   Q(description__contains=searched)
                                                   )

        girls_shorts = GirlsShort.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                 Q(style_no__contains=searched) |
                                                 Q(fabric_id__contains=searched) |
                                                 Q(fabric_price__contains=searched) |
                                                 Q(consumption__contains=searched) |
                                                 Q(acc_name__contains=searched) |
                                                 Q(acc_id__contains=searched) |
                                                 Q(acc_cost__contains=searched) |
                                                 Q(sewing_cost__contains=searched) |
                                                 Q(embroidery_cost__contains=searched) |
                                                 Q(washed_cost__contains=searched) |
                                                 Q(paint_cost__contains=searched) |
                                                 Q(factory_profit__contains=searched) |
                                                 Q(total_value__contains=searched) |
                                                 Q(accepted__contains=searched) |
                                                 Q(description__contains=searched)
                                                 )

        # infants
        infants_frocks = InfantsFrock.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                     Q(style_no__contains=searched) |
                                                     Q(fabric_id__contains=searched) |
                                                     Q(fabric_price__contains=searched) |
                                                     Q(consumption__contains=searched) |
                                                     Q(acc_name__contains=searched) |
                                                     Q(acc_id__contains=searched) |
                                                     Q(acc_cost__contains=searched) |
                                                     Q(sewing_cost__contains=searched) |
                                                     Q(embroidery_cost__contains=searched) |
                                                     Q(washed_cost__contains=searched) |
                                                     Q(paint_cost__contains=searched) |
                                                     Q(factory_profit__contains=searched) |
                                                     Q(total_value__contains=searched) |
                                                     Q(accepted__contains=searched) |
                                                     Q(description__contains=searched)
                                                     )

        infants_pants = InfantsPant.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                   Q(style_no__contains=searched) |
                                                   Q(fabric_id__contains=searched) |
                                                   Q(fabric_price__contains=searched) |
                                                   Q(consumption__contains=searched) |
                                                   Q(acc_name__contains=searched) |
                                                   Q(acc_id__contains=searched) |
                                                   Q(acc_cost__contains=searched) |
                                                   Q(sewing_cost__contains=searched) |
                                                   Q(embroidery_cost__contains=searched) |
                                                   Q(washed_cost__contains=searched) |
                                                   Q(paint_cost__contains=searched) |
                                                   Q(factory_profit__contains=searched) |
                                                   Q(total_value__contains=searched) |
                                                   Q(accepted__contains=searched) |
                                                   Q(description__contains=searched)
                                                   )

        # teens
        teens_frocks = Teenfrock.objects.filter(Q(sample_manufactured_date__contains=searched) |
                                                Q(style_no__contains=searched) |
                                                Q(fabric_id__contains=searched) |
                                                Q(fabric_price__contains=searched) |
                                                Q(consumption__contains=searched) |
                                                Q(acc_name__contains=searched) |
                                                Q(acc_id__contains=searched) |
                                                Q(acc_cost__contains=searched) |
                                                Q(sewing_cost__contains=searched) |
                                                Q(embroidery_cost__contains=searched) |
                                                Q(washed_cost__contains=searched) |
                                                Q(paint_cost__contains=searched) |
                                                Q(factory_profit__contains=searched) |
                                                Q(total_value__contains=searched) |
                                                Q(accepted__contains=searched) |
                                                Q(description__contains=searched)
                                                )

        sewings = Sewing.objects.filter(Q(order_received__contains=searched) |
                                        Q(date_order_delivered__contains=searched) |
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
                                        Q(remarks__contains=searched) |
                                        Q(required_date__contains=searched) |
                                        Q(order_accepted__contains=searched) |
                                        Q(order_progress__contains=searched) |
                                        Q(completed_date__contains=searched) |
                                        Q(release_date__contains=searched) |
                                        Q(reason__contains=searched)
                                        )

        # products
        # ladies
        ladies_frock_products = LadiesFrockProduct.objects.filter(Q(product_name__contains=searched) |
                                                                  Q(product_id__contains=searched) |
                                                                  Q(product_manufacture_date__contains=searched) |
                                                                  Q(sample_id__contains=searched) |
                                                                  Q(sample_created_date__contains=searched) |
                                                                  Q(fabric_name__contains=searched) |
                                                                  Q(fabric_id__contains=searched) |
                                                                  Q(fabric_supplied_date__contains=searched) |
                                                                  Q(total_quantity__contains=searched) |
                                                                  Q(total_price__contains=searched) |
                                                                  Q(customer__customer_id__contains=searched) |
                                                                  Q(customer__salutation__contains=searched) |
                                                                  Q(customer__customer_first_name__contains=searched) |
                                                                  Q(customer__customer_last_name__contains=searched) |
                                                                  Q(customer__mobile_no__contains=searched) |
                                                                  Q(customer__mobile_no_type__contains=searched) |
                                                                  Q(customer__email__contains=searched) |
                                                                  Q(customer__email_type__contains=searched) |
                                                                  Q(customer__address__contains=searched) |
                                                                  Q(approved_by__contains=searched) |
                                                                  Q(approved_on__contains=searched) |
                                                                  Q(notes__contains=searched)
                                                                  )

        ladies_blouse_products = LadiesBlouseProduct.objects.filter(Q(product_name__contains=searched) |
                                                                    Q(product_id__contains=searched) |
                                                                    Q(product_manufacture_date__contains=searched) |
                                                                    Q(sample_id__contains=searched) |
                                                                    Q(sample_created_date__contains=searched) |
                                                                    Q(fabric_name__contains=searched) |
                                                                    Q(fabric_id__contains=searched) |
                                                                    Q(fabric_supplied_date__contains=searched) |
                                                                    Q(total_quantity__contains=searched) |
                                                                    Q(total_price__contains=searched) |
                                                                    Q(customer__customer_id__contains=searched) |
                                                                    Q(customer__salutation__contains=searched) |
                                                                    Q(
                                                                        customer__customer_first_name__contains=searched) |
                                                                    Q(customer__customer_last_name__contains=searched) |
                                                                    Q(customer__mobile_no__contains=searched) |
                                                                    Q(customer__mobile_no_type__contains=searched) |
                                                                    Q(customer__email__contains=searched) |
                                                                    Q(customer__email_type__contains=searched) |
                                                                    Q(customer__address__contains=searched) |
                                                                    Q(approved_by__contains=searched) |
                                                                    Q(approved_on__contains=searched) |
                                                                    Q(notes__contains=searched)
                                                                    )

        ladies_skirt_products = LadiesSkirtProduct.objects.filter(Q(product_name__contains=searched) |
                                                                  Q(product_id__contains=searched) |
                                                                  Q(product_manufacture_date__contains=searched) |
                                                                  Q(sample_id__contains=searched) |
                                                                  Q(sample_created_date__contains=searched) |
                                                                  Q(fabric_name__contains=searched) |
                                                                  Q(fabric_id__contains=searched) |
                                                                  Q(fabric_supplied_date__contains=searched) |
                                                                  Q(total_quantity__contains=searched) |
                                                                  Q(total_price__contains=searched) |
                                                                  Q(customer__customer_id__contains=searched) |
                                                                  Q(customer__salutation__contains=searched) |
                                                                  Q(customer__customer_first_name__contains=searched) |
                                                                  Q(customer__customer_last_name__contains=searched) |
                                                                  Q(customer__mobile_no__contains=searched) |
                                                                  Q(customer__mobile_no_type__contains=searched) |
                                                                  Q(customer__email__contains=searched) |
                                                                  Q(customer__email_type__contains=searched) |
                                                                  Q(customer__address__contains=searched) |
                                                                  Q(approved_by__contains=searched) |
                                                                  Q(approved_on__contains=searched) |
                                                                  Q(notes__contains=searched)
                                                                  )

        ladies_tshirt_products = LadiesTshirtProduct.objects.filter(Q(product_name__contains=searched) |
                                                                    Q(product_id__contains=searched) |
                                                                    Q(product_manufacture_date__contains=searched) |
                                                                    Q(sample_id__contains=searched) |
                                                                    Q(sample_created_date__contains=searched) |
                                                                    Q(fabric_name__contains=searched) |
                                                                    Q(fabric_id__contains=searched) |
                                                                    Q(fabric_supplied_date__contains=searched) |
                                                                    Q(total_quantity__contains=searched) |
                                                                    Q(total_price__contains=searched) |
                                                                    Q(customer__customer_id__contains=searched) |
                                                                    Q(customer__salutation__contains=searched) |
                                                                    Q(
                                                                        customer__customer_first_name__contains=searched) |
                                                                    Q(customer__customer_last_name__contains=searched) |
                                                                    Q(customer__mobile_no__contains=searched) |
                                                                    Q(customer__mobile_no_type__contains=searched) |
                                                                    Q(customer__email__contains=searched) |
                                                                    Q(customer__email_type__contains=searched) |
                                                                    Q(customer__address__contains=searched) |
                                                                    Q(approved_by__contains=searched) |
                                                                    Q(approved_on__contains=searched) |
                                                                    Q(notes__contains=searched)
                                                                    )

        maternity_frock_products = MaternityFrockProduct.objects.filter(Q(product_name__contains=searched) |
                                                                        Q(product_id__contains=searched) |
                                                                        Q(product_manufacture_date__contains=searched) |
                                                                        Q(sample_id__contains=searched) |
                                                                        Q(sample_created_date__contains=searched) |
                                                                        Q(fabric_name__contains=searched) |
                                                                        Q(fabric_id__contains=searched) |
                                                                        Q(fabric_supplied_date__contains=searched) |
                                                                        Q(total_quantity__contains=searched) |
                                                                        Q(total_price__contains=searched) |
                                                                        Q(customer__customer_id__contains=searched) |
                                                                        Q(customer__salutation__contains=searched) |
                                                                        Q(
                                                                            customer__customer_first_name__contains=searched) |
                                                                        Q(
                                                                            customer__customer_last_name__contains=searched) |
                                                                        Q(customer__mobile_no__contains=searched) |
                                                                        Q(customer__mobile_no_type__contains=searched) |
                                                                        Q(customer__email__contains=searched) |
                                                                        Q(customer__email_type__contains=searched) |
                                                                        Q(customer__address__contains=searched) |
                                                                        Q(approved_by__contains=searched) |
                                                                        Q(approved_on__contains=searched) |
                                                                        Q(notes__contains=searched)
                                                                        )

        kaftan_products = KaftanProduct.objects.filter(Q(product_name__contains=searched) |
                                                       Q(product_id__contains=searched) |
                                                       Q(product_manufacture_date__contains=searched) |
                                                       Q(sample_id__contains=searched) |
                                                       Q(sample_created_date__contains=searched) |
                                                       Q(fabric_name__contains=searched) |
                                                       Q(fabric_id__contains=searched) |
                                                       Q(fabric_supplied_date__contains=searched) |
                                                       Q(total_quantity__contains=searched) |
                                                       Q(total_price__contains=searched) |
                                                       Q(customer__customer_id__contains=searched) |
                                                       Q(customer__salutation__contains=searched) |
                                                       Q(customer__customer_first_name__contains=searched) |
                                                       Q(customer__customer_last_name__contains=searched) |
                                                       Q(customer__mobile_no__contains=searched) |
                                                       Q(customer__mobile_no_type__contains=searched) |
                                                       Q(customer__email__contains=searched) |
                                                       Q(customer__email_type__contains=searched) |
                                                       Q(customer__address__contains=searched) |
                                                       Q(approved_by__contains=searched) |
                                                       Q(approved_on__contains=searched) |
                                                       Q(notes__contains=searched)
                                                       )

        nightwear_products = NightwearProduct.objects.filter(Q(product_name__contains=searched) |
                                                             Q(product_id__contains=searched) |
                                                             Q(product_manufacture_date__contains=searched) |
                                                             Q(sample_id__contains=searched) |
                                                             Q(sample_created_date__contains=searched) |
                                                             Q(fabric_name__contains=searched) |
                                                             Q(fabric_id__contains=searched) |
                                                             Q(fabric_supplied_date__contains=searched) |
                                                             Q(total_quantity__contains=searched) |
                                                             Q(total_price__contains=searched) |
                                                             Q(customer__customer_id__contains=searched) |
                                                             Q(customer__salutation__contains=searched) |
                                                             Q(customer__customer_first_name__contains=searched) |
                                                             Q(customer__customer_last_name__contains=searched) |
                                                             Q(customer__mobile_no__contains=searched) |
                                                             Q(customer__mobile_no_type__contains=searched) |
                                                             Q(customer__email__contains=searched) |
                                                             Q(customer__email_type__contains=searched) |
                                                             Q(customer__address__contains=searched) |
                                                             Q(approved_by__contains=searched) |
                                                             Q(approved_on__contains=searched) |
                                                             Q(notes__contains=searched)
                                                             )

        # boys
        boys_pant_products = BoysPantProduct.objects.filter(Q(product_name__contains=searched) |
                                                            Q(product_id__contains=searched) |
                                                            Q(product_manufacture_date__contains=searched) |
                                                            Q(sample_id__contains=searched) |
                                                            Q(sample_created_date__contains=searched) |
                                                            Q(fabric_name__contains=searched) |
                                                            Q(fabric_id__contains=searched) |
                                                            Q(fabric_supplied_date__contains=searched) |
                                                            Q(total_quantity__contains=searched) |
                                                            Q(total_price__contains=searched) |
                                                            Q(customer__customer_id__contains=searched) |
                                                            Q(customer__salutation__contains=searched) |
                                                            Q(customer__customer_first_name__contains=searched) |
                                                            Q(customer__customer_last_name__contains=searched) |
                                                            Q(customer__mobile_no__contains=searched) |
                                                            Q(customer__mobile_no_type__contains=searched) |
                                                            Q(customer__email__contains=searched) |
                                                            Q(customer__email_type__contains=searched) |
                                                            Q(customer__address__contains=searched) |
                                                            Q(approved_by__contains=searched) |
                                                            Q(approved_on__contains=searched) |
                                                            Q(notes__contains=searched)
                                                            )

        boys_shirt_products = BoysShirtProduct.objects.filter(Q(product_name__contains=searched) |
                                                              Q(product_id__contains=searched) |
                                                              Q(product_manufacture_date__contains=searched) |
                                                              Q(sample_id__contains=searched) |
                                                              Q(sample_created_date__contains=searched) |
                                                              Q(fabric_name__contains=searched) |
                                                              Q(fabric_id__contains=searched) |
                                                              Q(fabric_supplied_date__contains=searched) |
                                                              Q(total_quantity__contains=searched) |
                                                              Q(total_price__contains=searched) |
                                                              Q(customer__customer_id__contains=searched) |
                                                              Q(customer__salutation__contains=searched) |
                                                              Q(customer__customer_first_name__contains=searched) |
                                                              Q(customer__customer_last_name__contains=searched) |
                                                              Q(customer__mobile_no__contains=searched) |
                                                              Q(customer__mobile_no_type__contains=searched) |
                                                              Q(customer__email__contains=searched) |
                                                              Q(customer__email_type__contains=searched) |
                                                              Q(customer__address__contains=searched) |
                                                              Q(approved_by__contains=searched) |
                                                              Q(approved_on__contains=searched) |
                                                              Q(notes__contains=searched)
                                                              )

        boys_tshirt_products = BoysTshirtProduct.objects.filter(Q(product_name__contains=searched) |
                                                                Q(product_id__contains=searched) |
                                                                Q(product_manufacture_date__contains=searched) |
                                                                Q(sample_id__contains=searched) |
                                                                Q(sample_created_date__contains=searched) |
                                                                Q(fabric_name__contains=searched) |
                                                                Q(fabric_id__contains=searched) |
                                                                Q(fabric_supplied_date__contains=searched) |
                                                                Q(total_quantity__contains=searched) |
                                                                Q(total_price__contains=searched) |
                                                                Q(customer__customer_id__contains=searched) |
                                                                Q(customer__salutation__contains=searched) |
                                                                Q(customer__customer_first_name__contains=searched) |
                                                                Q(customer__customer_last_name__contains=searched) |
                                                                Q(customer__mobile_no__contains=searched) |
                                                                Q(customer__mobile_no_type__contains=searched) |
                                                                Q(customer__email__contains=searched) |
                                                                Q(customer__email_type__contains=searched) |
                                                                Q(customer__address__contains=searched) |
                                                                Q(approved_by__contains=searched) |
                                                                Q(approved_on__contains=searched) |
                                                                Q(notes__contains=searched)
                                                                )

        boys_short_products = BoysShortProduct.objects.filter(Q(product_name__contains=searched) |
                                                              Q(product_id__contains=searched) |
                                                              Q(product_manufacture_date__contains=searched) |
                                                              Q(sample_id__contains=searched) |
                                                              Q(sample_created_date__contains=searched) |
                                                              Q(fabric_name__contains=searched) |
                                                              Q(fabric_id__contains=searched) |
                                                              Q(fabric_supplied_date__contains=searched) |
                                                              Q(total_quantity__contains=searched) |
                                                              Q(total_price__contains=searched) |
                                                              Q(customer__customer_id__contains=searched) |
                                                              Q(customer__salutation__contains=searched) |
                                                              Q(customer__customer_first_name__contains=searched) |
                                                              Q(customer__customer_last_name__contains=searched) |
                                                              Q(customer__mobile_no__contains=searched) |
                                                              Q(customer__mobile_no_type__contains=searched) |
                                                              Q(customer__email__contains=searched) |
                                                              Q(customer__email_type__contains=searched) |
                                                              Q(customer__address__contains=searched) |
                                                              Q(approved_by__contains=searched) |
                                                              Q(approved_on__contains=searched) |
                                                              Q(notes__contains=searched)
                                                              )

        # girls
        girls_frock_products = GirlsFrockProduct.objects.filter(Q(product_name__contains=searched) |
                                                                Q(product_id__contains=searched) |
                                                                Q(product_manufacture_date__contains=searched) |
                                                                Q(sample_id__contains=searched) |
                                                                Q(sample_created_date__contains=searched) |
                                                                Q(fabric_name__contains=searched) |
                                                                Q(fabric_id__contains=searched) |
                                                                Q(fabric_supplied_date__contains=searched) |
                                                                Q(total_quantity__contains=searched) |
                                                                Q(total_price__contains=searched) |
                                                                Q(customer__customer_id__contains=searched) |
                                                                Q(customer__salutation__contains=searched) |
                                                                Q(customer__customer_first_name__contains=searched) |
                                                                Q(customer__customer_last_name__contains=searched) |
                                                                Q(customer__mobile_no__contains=searched) |
                                                                Q(customer__mobile_no_type__contains=searched) |
                                                                Q(customer__email__contains=searched) |
                                                                Q(customer__email_type__contains=searched) |
                                                                Q(customer__address__contains=searched) |
                                                                Q(approved_by__contains=searched) |
                                                                Q(approved_on__contains=searched) |
                                                                Q(notes__contains=searched)
                                                                )

        girls_pant_products = GirlsPantProduct.objects.filter(Q(product_name__contains=searched) |
                                                              Q(product_id__contains=searched) |
                                                              Q(product_manufacture_date__contains=searched) |
                                                              Q(sample_id__contains=searched) |
                                                              Q(sample_created_date__contains=searched) |
                                                              Q(fabric_name__contains=searched) |
                                                              Q(fabric_id__contains=searched) |
                                                              Q(fabric_supplied_date__contains=searched) |
                                                              Q(total_quantity__contains=searched) |
                                                              Q(total_price__contains=searched) |
                                                              Q(customer__customer_id__contains=searched) |
                                                              Q(customer__salutation__contains=searched) |
                                                              Q(customer__customer_first_name__contains=searched) |
                                                              Q(customer__customer_last_name__contains=searched) |
                                                              Q(customer__mobile_no__contains=searched) |
                                                              Q(customer__mobile_no_type__contains=searched) |
                                                              Q(customer__email__contains=searched) |
                                                              Q(customer__email_type__contains=searched) |
                                                              Q(customer__address__contains=searched) |
                                                              Q(approved_by__contains=searched) |
                                                              Q(approved_on__contains=searched) |
                                                              Q(notes__contains=searched)
                                                              )

        girls_tshirt_products = GirlsTshirtProduct.objects.filter(Q(product_name__contains=searched) |
                                                                  Q(product_id__contains=searched) |
                                                                  Q(product_manufacture_date__contains=searched) |
                                                                  Q(sample_id__contains=searched) |
                                                                  Q(sample_created_date__contains=searched) |
                                                                  Q(fabric_name__contains=searched) |
                                                                  Q(fabric_id__contains=searched) |
                                                                  Q(fabric_supplied_date__contains=searched) |
                                                                  Q(total_quantity__contains=searched) |
                                                                  Q(total_price__contains=searched) |
                                                                  Q(customer__customer_id__contains=searched) |
                                                                  Q(customer__salutation__contains=searched) |
                                                                  Q(customer__customer_first_name__contains=searched) |
                                                                  Q(customer__customer_last_name__contains=searched) |
                                                                  Q(customer__mobile_no__contains=searched) |
                                                                  Q(customer__mobile_no_type__contains=searched) |
                                                                  Q(customer__email__contains=searched) |
                                                                  Q(customer__email_type__contains=searched) |
                                                                  Q(customer__address__contains=searched) |
                                                                  Q(approved_by__contains=searched) |
                                                                  Q(approved_on__contains=searched) |
                                                                  Q(notes__contains=searched)
                                                                  )

        girls_short_products = GirlsShortproduct.objects.filter(Q(product_name__contains=searched) |
                                                                Q(product_id__contains=searched) |
                                                                Q(product_manufacture_date__contains=searched) |
                                                                Q(sample_id__contains=searched) |
                                                                Q(sample_created_date__contains=searched) |
                                                                Q(fabric_name__contains=searched) |
                                                                Q(fabric_id__contains=searched) |
                                                                Q(fabric_supplied_date__contains=searched) |
                                                                Q(total_quantity__contains=searched) |
                                                                Q(total_price__contains=searched) |
                                                                Q(customer__customer_id__contains=searched) |
                                                                Q(customer__salutation__contains=searched) |
                                                                Q(customer__customer_first_name__contains=searched) |
                                                                Q(customer__customer_last_name__contains=searched) |
                                                                Q(customer__mobile_no__contains=searched) |
                                                                Q(customer__mobile_no_type__contains=searched) |
                                                                Q(customer__email__contains=searched) |
                                                                Q(customer__email_type__contains=searched) |
                                                                Q(customer__address__contains=searched) |
                                                                Q(approved_by__contains=searched) |
                                                                Q(approved_on__contains=searched) |
                                                                Q(notes__contains=searched)
                                                                )

        # infants
        # frock
        infants_frock_products = InfantsFrockProduct.objects.filter(Q(product_name__contains=searched) |
                                                                    Q(product_id__contains=searched) |
                                                                    Q(product_manufacture_date__contains=searched) |
                                                                    Q(sample_id__contains=searched) |
                                                                    Q(sample_created_date__contains=searched) |
                                                                    Q(fabric_name__contains=searched) |
                                                                    Q(fabric_id__contains=searched) |
                                                                    Q(fabric_supplied_date__contains=searched) |
                                                                    Q(total_quantity__contains=searched) |
                                                                    Q(total_price__contains=searched) |
                                                                    Q(customer__customer_id__contains=searched) |
                                                                    Q(customer__salutation__contains=searched) |
                                                                    Q(
                                                                        customer__customer_first_name__contains=searched) |
                                                                    Q(customer__customer_last_name__contains=searched) |
                                                                    Q(customer__mobile_no__contains=searched) |
                                                                    Q(customer__mobile_no_type__contains=searched) |
                                                                    Q(customer__email__contains=searched) |
                                                                    Q(customer__email_type__contains=searched) |
                                                                    Q(customer__address__contains=searched) |
                                                                    Q(approved_by__contains=searched) |
                                                                    Q(approved_on__contains=searched) |
                                                                    Q(notes__contains=searched)
                                                                    )

        infants_pant_products = InfantsPantProduct.objects.filter(Q(product_name__contains=searched) |
                                                                  Q(product_id__contains=searched) |
                                                                  Q(product_manufacture_date__contains=searched) |
                                                                  Q(sample_id__contains=searched) |
                                                                  Q(sample_created_date__contains=searched) |
                                                                  Q(fabric_name__contains=searched) |
                                                                  Q(fabric_id__contains=searched) |
                                                                  Q(fabric_supplied_date__contains=searched) |
                                                                  Q(total_quantity__contains=searched) |
                                                                  Q(total_price__contains=searched) |
                                                                  Q(customer__customer_id__contains=searched) |
                                                                  Q(customer__salutation__contains=searched) |
                                                                  Q(customer__customer_first_name__contains=searched) |
                                                                  Q(customer__customer_last_name__contains=searched) |
                                                                  Q(customer__mobile_no__contains=searched) |
                                                                  Q(customer__mobile_no_type__contains=searched) |
                                                                  Q(customer__email__contains=searched) |
                                                                  Q(customer__email_type__contains=searched) |
                                                                  Q(customer__address__contains=searched) |
                                                                  Q(approved_by__contains=searched) |
                                                                  Q(approved_on__contains=searched) |
                                                                  Q(notes__contains=searched)
                                                                  )

        # teens
        teens_frock_products = TeensFrockProduct.objects.filter(Q(product_name__contains=searched) |
                                                                Q(product_id__contains=searched) |
                                                                Q(product_manufacture_date__contains=searched) |
                                                                Q(sample_id__contains=searched) |
                                                                Q(sample_created_date__contains=searched) |
                                                                Q(fabric_name__contains=searched) |
                                                                Q(fabric_id__contains=searched) |
                                                                Q(fabric_supplied_date__contains=searched) |
                                                                Q(total_quantity__contains=searched) |
                                                                Q(total_price__contains=searched) |
                                                                Q(customer__customer_id__contains=searched) |
                                                                Q(customer__salutation__contains=searched) |
                                                                Q(customer__customer_first_name__contains=searched) |
                                                                Q(customer__customer_last_name__contains=searched) |
                                                                Q(customer__mobile_no__contains=searched) |
                                                                Q(customer__mobile_no_type__contains=searched) |
                                                                Q(customer__email__contains=searched) |
                                                                Q(customer__email_type__contains=searched) |
                                                                Q(customer__address__contains=searched) |
                                                                Q(approved_by__contains=searched) |
                                                                Q(approved_on__contains=searched) |
                                                                Q(notes__contains=searched)
                                                                )

    context = {
        'searched': searched,

        'customers': customers,

        'accessories_received_ins': accessories_received_ins,
        'accessories_sent_outs': accessories_sent_outs,

        'fabric_order_ins': fabric_order_ins,
        'fabric_order_outs': fabric_order_outs,

        'invoices': invoices,

        'order_receivings': order_receivings,

        'ladies_frocks': ladies_frocks,
        'ladies_blouses': ladies_blouses,
        'ladies_skirts': ladies_skirts,
        'ladies_pants': ladies_pants,
        'maternity_frocks': maternity_frocks,
        'kaftans': kaftans,
        'ladies_tshirts': ladies_tshirts,
        'nightwears': nightwears,

        'boys_pants': boys_pants,
        'boys_shirts': boys_shirts,
        'boys_tshirts': boys_tshirts,
        'boys_shorts': boys_shorts,

        'girls_frocks': girls_frocks,
        'girls_pants': girls_pants,
        'girls_tshirts': girls_tshirts,
        'girls_shorts': girls_shorts,

        'infants_frocks': infants_frocks,
        'infants_pants': infants_pants,

        'teens_frocks': teens_frocks,

        'sewings': sewings,

        # products
        # ladies
        'ladies_frock_products': ladies_frock_products,
        'ladies_blouse_products': ladies_blouse_products,
        'ladies_skirt_products': ladies_skirt_products,
        'ladies_tshirt_products': ladies_tshirt_products,
        'maternity_frock_products': maternity_frock_products,
        'kaftan_products': kaftan_products,
        'nightwear_products': nightwear_products,

        # boys
        'boys_pant_products': boys_pant_products,
        'boys_shirt_products': boys_shirt_products,
        'boys_tshirt_products': boys_tshirt_products,
        'boys_short_products': boys_short_products,

        # girls
        'girls_frock_products': girls_frock_products,
        'girls_pant_products': girls_pant_products,
        'girls_tshirt_products': girls_tshirt_products,
        'girls_short_products': girls_short_products,

        # infants
        'infants_frock_products': infants_frock_products,
        'infants_pant_products': infants_pant_products,

        # teens
        'teens_frock_products': teens_frock_products,
    }

    return render(request, template_name, context)
