from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import Http404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None

    return formcls(data, prefix=prefix)


def _get_edit_form(request, form_cls, instance,prefix):
    data = request.POST if prefix in request.POST else None

    return form_cls(data, instance=instance, prefix=prefix)


@method_decorator(login_required(login_url='../users/login'), name='get')
class ProductsMainView(View):
    template_name = 'products_main.html'

    # Ladies
    ladies_frock_queryset = LadiesFrock.objects.all()
    ladies_blouse_queryset = LadiesBlouse.objects.all()
    ladies_pant_queryset = LadiesPant.objects.all()
    ladies_skirt_queryset = LadiesSkirt.objects.all()
    ladies_tshirt_queryset = LadiesTshirt.objects.all()
    maternity_frock_queryset = MaternityFrock.objects.all()
    kaftan_queryset = Kaftan.objects.all()
    nightwear_queryset = Nightwear.objects.all()

    def get_ladies_frock_queryset(self):
        return self.ladies_frock_queryset

    def get_ladies_blouse_queryset(self):
        return self.ladies_blouse_queryset

    def get_ladies_pant_queryset(self):
        return self.ladies_pant_queryset

    def get_ladies_skirt_queryset(self):
        return self.ladies_skirt_queryset

    def get_ladies_tshirt_queryset(self):
        return self.ladies_tshirt_queryset

    def get_maternity_frock_queryset(self):
        return self.maternity_frock_queryset

    def get_kaftan_queryset(self):
        return self.kaftan_queryset

    def get_nightwear_queryset(self):
        return self.nightwear_queryset

    # Boys
    boys_pant_queryset = BoysPant.objects.all()
    boys_shirt_queryset = BoysShirt.objects.all()
    boys_tshirt_queryset = BoysTshirt.objects.all()
    boys_short_queryset = BoysShort.objects.all()

    def get_boys_pant_queryset(self):
        return self.boys_pant_queryset

    def get_boys_shirt_queryset(self):
        return self.boys_shirt_queryset

    def get_boys_tshirt_queryset(self):
        return self.boys_tshirt_queryset

    def get_boys_short_queryset(self):
        return self.boys_short_queryset

    # Girls
    girls_frock_queryset = GirlsFrock.objects.all()
    girls_pant_queryset = GirlsPant.objects.all()
    girls_tshirt_queryset = GirlsTshirt.objects.all()
    girls_short_queryset = GirlsShort.objects.all()

    def get_girls_frock_queryset(self):
        return self.girls_frock_queryset

    def get_girls_pant_queryset(self):
        return self.girls_pant_queryset

    def get_girls_tshirt_queryset(self):
        return self.girls_tshirt_queryset

    def get_girls_short_queryset(self):
        return self.girls_short_queryset

    # Infants
    infants_frock_queryset = InfantsFrock.objects.all()
    infants_pant_queryset = InfantsPant.objects.all()

    def get_infants_frock_queryset(self):
        return self.infants_frock_queryset

    def get_infants_pant_queryset(self):
        return self.infants_pant_queryset

    # Teens
    teen_frock_queryset = TeenFrock.objects.all()

    def get_teen_frock_queryset(self):
        return self.teen_frock_queryset

    def get(self, request):
        # Forms

        # Ladies
        ladies_frock_form = LadiesFrockForm(prefix='ladies-frock')
        ladies_blouse_form = LadiesBlouseForm(prefix='ladies-blouse')
        ladies_pant_form = LadiesPantForm(prefix='ladies-pant')
        ladies_skirt_form = LadiesSkirtForm(prefix='ladies-skirt')
        ladies_tshirt_form = LadiesTshirtForm(prefix='ladies-tshirt')
        maternity_frock_form = MaternityFrockForm(prefix='maternity-frock')
        kaftan_form = KaftanForm(prefix='kaftan')
        nightwear_form = NightwearForm(prefix='nightwear')

        # Boys
        boys_pant_form = BoysPantForm(prefix='boys-pant')
        boys_shirt_form = BoysShirtForm(prefix='boys-shirt')
        boys_tshirt_form = BoysTshirtForm(prefix='boys-tshirt')
        boys_short_form = BoysShortForm(prefix='boys-short')

        # Girls
        girls_frock_form = GirlsFrockForm(prefix='girls-frock')
        girls_pant_form = GirlsPantForm(prefix='girls-pant')
        girls_tshirt_form = GirlsTshirtForm(prefix='girls-tshirt')
        girls_short_form = GirlsShortForm(prefix='girls-short')

        # Infants
        infants_frock_form = InfantsFrockForm(prefix='infants-frock')
        infants_pant_form = InfantsPantForm(prefix='infants-pant')

        # Teens
        teens_frock_form = TeenFrockForm(prefix='teen-frock')

        context = {
            # Ladies
            'ladies_frocks': self.get_ladies_frock_queryset(),
            'ladies_blouses': self.get_ladies_blouse_queryset(),
            'ladies_pants': self.get_ladies_pant_queryset(),
            'ladies_skirts': self.get_ladies_skirt_queryset(),
            'ladies_tshirts': self.get_ladies_tshirt_queryset(),
            'maternity_frocks': self.get_maternity_frock_queryset(),
            'kaftans': self.get_kaftan_queryset(),
            'nightwears': self.get_nightwear_queryset(),

            'ladies_frock_form': ladies_frock_form,
            'ladies_blouse_form': ladies_blouse_form,
            'ladies_skirt_form': ladies_skirt_form,
            'ladies_pant_form': ladies_pant_form,
            'ladies_tshirt_form': ladies_tshirt_form,
            'maternity_frock_form': maternity_frock_form,
            'kaftan_form': kaftan_form,
            'nightwear_form': nightwear_form,

            # Boys
            'boys_pants': self.get_boys_pant_queryset(),
            'boys_shirts': self.get_boys_shirt_queryset(),
            'boys_tshirts': self.get_boys_tshirt_queryset(),
            'boys_shorts': self.get_boys_short_queryset(),

            'boys_pant_form': boys_pant_form,
            'boys_shirt_form': boys_shirt_form,
            'boys_tshirt_form': boys_tshirt_form,
            'boys_short_form': boys_short_form,

            # Girls
            'girls_frocks': self.get_girls_frock_queryset(),
            'girls_pants': self.get_girls_pant_queryset(),
            'girls_tshirts': self.get_girls_tshirt_queryset(),
            'girls_shorts': self.get_girls_short_queryset(),

            'girls_frock_form': girls_frock_form,
            'girls_pant_form': girls_pant_form,
            'girls_tshirt_form': girls_tshirt_form,
            'girls_short_form': girls_short_form,

            # Infants
            'infants_frocks': self.get_infants_frock_queryset(),
            'infants_pants': self.get_infants_pant_queryset(),

            'infants_frock_form': infants_frock_form,
            'infants_pant_form': infants_pant_form,

            # Teens
            'teen_frocks': self.get_teen_frock_queryset(),

            'teens_frock_form': teens_frock_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # Ladies
        ladies_frock_form = _get_form(request, LadiesFrockForm, 'ladies-frock')
        ladies_blouse_form = _get_form(request, LadiesBlouseForm, 'ladies-blouse')
        ladies_skirt_form = _get_form(request, LadiesSkirtForm, 'ladies-skirt')
        ladies_pant_form = _get_form(request, LadiesPantForm, 'ladies-pant')
        ladies_tshirt_form = _get_form(request, LadiesTshirtForm, 'ladies-tshirt')
        maternity_frock_form = _get_form(request, MaternityFrockForm, 'maternity-frock')
        kaftan_form = _get_form(request, KaftanForm, 'kaftan')
        nightwear_form = _get_form(request, NightwearForm, 'nightwear')

        # Boys
        boys_pant_form = _get_form(request, BoysPantForm, 'boys-pant')
        boys_shirt_form = _get_form(request, BoysShirtForm, 'boys-shirt')
        boys_tshirt_form = _get_form(request, BoysTshirtForm, 'boys-tshirt')
        boys_short_form = _get_form(request, BoysShortForm, 'boys-short')

        # Girls
        girls_frock_form = _get_form(request, GirlsFrockForm, 'girls-frock')
        girls_pant_form = _get_form(request, GirlsPantForm, 'girls-pant')
        girls_tshirt_form = _get_form(request, GirlsTshirtForm, 'girls-tshirt')
        girls_short_form = _get_form(request, GirlsShortForm, 'girls-short')

        # Infants
        infants_frock_form = _get_form(request, InfantsFrockForm, 'infants-frock')
        infants_pant_form = _get_form(request, InfantsPantForm, 'infant-pant')

        # Teens
        teens_frock_form = _get_form(request, TeenFrockForm, 'teen-frock')

        if ladies_frock_form.is_bound and ladies_frock_form.is_valid():
            ladies_frock_form.save()
        elif ladies_blouse_form.is_bound and ladies_blouse_form.is_valid():
            ladies_blouse_form.save()
            ladies_blouse_form = LadiesBlouseForm()
        elif ladies_skirt_form.is_bound and ladies_skirt_form.is_valid():
            ladies_skirt_form.save()
            ladies_skirt_form = LadiesSkirtForm()
        elif ladies_pant_form.is_bound and ladies_pant_form.is_valid():
            ladies_pant_form.save()
            ladies_pant_form = LadiesPantForm()
        elif ladies_tshirt_form.is_bound and ladies_tshirt_form.is_valid():
            ladies_tshirt_form.save()
            ladies_tshirt_form = LadiesTshirtForm()
        elif maternity_frock_form.is_bound and ladies_pant_form.is_valid():
            maternity_frock_form.save()
            maternity_frock_form = MaternityFrockForm()
        elif nightwear_form.is_bound and nightwear_form.is_valid():
            nightwear_form.save()
            nightwear_form = NightwearForm()
        elif boys_pant_form.is_bound and boys_pant_form.is_valid():
            boys_pant_form.save()
            boys_pant_form = BoysPantForm()
        elif boys_shirt_form.is_bound and boys_shirt_form.is_valid():
            boys_shirt_form.save()
            boys_shirt_form = BoysShirtForm()
        elif boys_tshirt_form.is_bound and boys_tshirt_form.is_valid():
            boys_tshirt_form.save()
            boys_tshirt_form = BoysTshirtForm()
        elif boys_short_form.is_bound and boys_short_form.is_valid():
            boys_short_form.save()
            boys_short_form = BoysShortForm()
        elif girls_frock_form.is_bound and girls_frock_form.is_valid():
            girls_frock_form.save()
            girls_frock_form = GirlsFrockForm()
        elif girls_pant_form.is_bound and girls_pant_form.is_valid():
            girls_pant_form.save()
            girls_pant_form = GirlsPantForm()
        elif girls_tshirt_form.is_bound and girls_tshirt_form.is_valid():
            girls_tshirt_form.save()
            girls_tshirt_form = GirlsTshirtForm()
        elif girls_short_form.is_bound and girls_short_form.is_valid():
            girls_short_form.save()
            girls_short_form = GirlsShortForm()
        elif infants_frock_form.is_bound and infants_frock_form.is_valid():
            infants_frock_form.save()
            infants_frock_form = InfantsFrockForm()
        elif infants_pant_form.is_bound and infants_pant_form.is_valid():
            infants_pant_form.save()
            infants_pant_form = InfantsPantForm()
        elif teens_frock_form.is_bound and teens_frock_form.is_valid():
            teens_frock_form.save()
            teens_frock_form = TeenFrockForm()

        context = {
            # Ladies
            'ladies_frock_form': ladies_frock_form,
            'ladies_blouse_form': ladies_blouse_form,
            'ladies_skirt_form': ladies_skirt_form,
            'ladies_pant_form': ladies_pant_form,
            'ladies_tshirt_form': ladies_tshirt_form,
            'maternity_frock_form': maternity_frock_form,
            'kaftan_form': kaftan_form,
            'nightwear_form': nightwear_form,

            # Boys
            'boys_pant_form': boys_pant_form,
            'boys_shirt_form': boys_shirt_form,
            'boys_tshirt_form': boys_tshirt_form,
            'boys_short_form': boys_short_form,

            # Girls
            'girls_frock_form': girls_frock_form,
            'girls_pant_form': girls_pant_form,
            'girls_tshirt_form': girls_tshirt_form,
            'girls_short_form': girls_short_form,

            # Infants
            'infants_frock_form': infants_frock_form,
            'infants_pant_form': infants_pant_form,

            # Teens
            'teens_frock_form': teens_frock_form,
        }

        return render(request, self.template_name, context)


def edit_view(self, request, id):
    template_name = 'products_main.html'
    try:
        ladies_frock_object = LadiesFrock.objects.get(id=id)
    except LadiesFrock.DoesNotExist:
        raise Http404

    """ladies_frock_edit_form = _get_edit_form(request, LadiesFrockForm, instance=ladies_frock_object, prefix='ladies-frock')

    if ladies_frock_edit_form.is_bound and ladies_frock_edit_form.is_valid():
        ladies_frock_edit_form.save()
    else:
        ladies_frock_edit_form = LadiesFrockForm(instance=ladies_frock_object, prefix='ladies-frock-edit')"""

    if request.method == 'POST':
        ladies_frock_edit_form = LadiesFrockForm(data=request.POST, instance=ladies_frock_object)
        if ladies_frock_edit_form.is_valid():
            ladies_frock_edit_form.save()
    else:
        ladies_frock_edit_form = LadiesBlouseForm(instance=ladies_frock_object)

    context = {
        'ladies_frock_edit_form': ladies_frock_edit_form,
    }

    return render(request, template_name, context)



