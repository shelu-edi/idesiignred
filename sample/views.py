from django.shortcuts import render
from django.views import View
from django.http import Http404

from .models import *
from .forms import *

# Create your views here.


class SampleMainView(View):
	template_name = 'sample_main.html'

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
	teen_frock_queryset = Teenfrock.objects.all()

	def get_teen_frock_queryset(self):
		return self.teen_frock_queryset

	def get(self, request):
		# Forms

		# Ladies
		ladies_frock_form = LadiesFrockForm()
		ladies_blouse_form = LadiesBlouseForm()
		ladies_pant_form = LadiesPantForm()
		ladies_skirt_form = LadiesSkirtForm()
		ladies_tshirt_form = LadiesTshirtForm()
		maternity_frock_form = MaternityFrockForm()
		kaftan_form = KaftanForm()
		nightwear_form = NightwearForm()

		# Boys
		boys_pant_form = BoysPantForm()
		boys_shirt_form = BoysShirtForm()
		boys_tshirt_form = BoysTshirtForm()
		boys_short_form = BoysShortForm()

		# Girls
		girls_frock_form = GirlsFrockForm()
		girls_pant_form = GirlsPantForm()
		girls_tshirt_form = GirlsTshirtForm()
		girls_short_form = GirlsShortForm()

		# Infants
		infants_frock_form = InfantsFrockForm()
		infants_pant_form = InfantsPantForm()

		# Teens
		teens_frock_form = TeenfrockForm()

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
		# Ladies Frock
		ladies_frock_form = LadiesFrockForm(request.POST)
		if ladies_frock_form.is_valid():
			ladies_frock_form.save()
			ladies_frock_form = LadiesFrockForm()

		# Ladies Blouse
		ladies_blouse_form = LadiesBlouseForm(request.POST)
		if ladies_blouse_form.is_valid():
			ladies_blouse_form.save()
			ladies_blouse_form = LadiesBlouseForm()

		# Ladies Pant
		ladies_pant_form = LadiesPantForm(request.POST)
		if ladies_pant_form.is_valid():
			ladies_pant_form.save()
			ladies_pant_form = LadiesPantForm()

		# Ladies Skirt
		ladies_skirt_form = LadiesSkirtForm(request.POST)
		if ladies_skirt_form.is_valid():
			ladies_skirt_form.save()
			ladies_skirt_form = LadiesPantForm()

		# Ladies T-shirt
		ladies_tshirt_form = LadiesTshirtForm(request.POST)
		if ladies_tshirt_form.is_valid():
			ladies_tshirt_form.save()
			ladies_tshirt_form = LadiesTshirtForm()

		# Maternity Frock
		maternity_frock_form = MaternityFrockForm(request.POST)
		if maternity_frock_form.is_valid():
			maternity_frock_form.save()
			maternity_frock_form = MaternityFrockForm()

		# Kaftan
		kaftan_form = KaftanForm(request.POST)
		if kaftan_form.is_valid():
			kaftan_form.save()
			kaftan_form = KaftanForm

		# Nightwear
		nightwear_form = NightwearForm(request.POST)
		if nightwear_form.is_valid():
			nightwear_form.save()
			nightwear_form = NightwearForm()

		# Boys
		# Boys Pant
		boys_pant_form = BoysPantForm(request.POST)
		if boys_pant_form.is_valid():
			boys_pant_form.save()
			boys_pant_form = BoysPantForm()

		# Boys Shirt
		boys_shirt_form = BoysShirtForm(request.POST)
		if boys_shirt_form.is_valid():
			boys_shirt_form.save()
			boys_shirt_form = BoysShirtForm()

		# Boys T-shirt
		boys_tshirt_form = BoysTshirtForm(request.POST)
		if boys_tshirt_form.is_valid():
			boys_tshirt_form.save()
			boys_tshirt_form = BoysTshirtForm()

		# Boys Short
		boys_short_form = BoysShortForm(request.POST)
		if boys_short_form.is_valid():
			boys_short_form.save()
			boys_short_form = BoysShortForm()

		# Girls
		# Girls Frock
		girls_frock_form = GirlsFrockForm(request.POST)
		if girls_frock_form.is_valid():
			girls_frock_form.save()
			girls_frock_form = GirlsFrockForm()

		# Girls Pant
		girls_pant_form = GirlsPantForm(request.POST)
		if girls_pant_form.is_valid():
			girls_pant_form.save()
			girls_pant_form = GirlsPantForm()

		# Girls T-shirt
		girls_tshirt_form = GirlsTshirtForm(request.POST)
		if girls_tshirt_form.is_valid():
			girls_tshirt_form.save()
			girls_tshirt_form = GirlsTshirtForm()

		# Girls Short
		girls_short_form = GirlsShortForm(request.POST)
		if girls_short_form.is_valid():
			girls_short_form.save()
			girls_short_form = GirlsShortForm()

		# Infants
		# Infants Frock
		infants_frock_form = InfantsFrockForm(request.POST)
		if infants_frock_form.is_valid():
			infants_frock_form.save()
			infants_frock_form = InfantsFrockForm()

		# Infants Pant
		infants_pant_form = InfantsPantForm(request.POST)
		if infants_pant_form.is_valid():
			infants_pant_form.save()
			infants_pant_form = InfantsPantForm()

		# Teens
		# Teens Frock
		teens_frock_form = TeenfrockForm(request.POST)
		if teens_frock_form.is_valid():
			teens_frock_form.save()
			teens_frock_form = TeenfrockForm()

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


def ladies_frock_view(request, id):
	template_name = 'ladies/frock/ladies_frock.html'
	# queryset = LadiesFrock.objects.all()

	try:
		obj = LadiesFrock.objects.get(id=id)
	except LadiesFrock.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = LadiesFrockForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = LadiesFrockForm(instance=obj)

	context = {
		'form': form,
		'object': obj,
	}

	return render(request, template_name, context)


def ladies_frock_print_view(request, id):
	template_name = 'ladies/frock/ladies_frock_print.html'

	try:
		obj = LadiesFrock.objects.get(id=id)
	except LadiesFrock.DoesNotExist:
		raise Http404

	context = {
		'object': obj,
	}

	return render(request, template_name, context)


def ladies_blouse_view(request, id):
	template = 'ladies/blouse/ladies_blouse.html'

	try:
		obj = LadiesBlouse.objects.get(id=id)
	except LadiesBlouse.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = LadiesBlouseForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = LadiesBlouseForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def ladies_blouse_print_view(request, id):
	template = 'ladies/blouse/ladies_blouse_print.html'

	try:
		obj = LadiesBlouse.objects.get(id=id)
	except LadiesBlouse.DoesNotExist:
		raise Http404

	context = {
		'object': obj,
	}

	return render(request, template, context)


def ladies_pant_view(request, id):
	template = 'ladies/pant/ladies_pant.html'

	try:
		obj = LadiesPant.objects.get(id=id)
	except LadiesPant.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = LadiesPantForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = LadiesPantForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def ladies_pant_print_view(request, id):
	template = 'ladies/pant/ladies_pant_print.html'

	try:
		obj = LadiesPant.objects.get(id=id)
	except LadiesPant.DoesNotExist:
		raise Http404

	context = {
		'object': obj,
	}

	return render(request, template, context)


def ladies_skirt_view(request, id):
	template = 'ladies/skirt/ladies_skirt.html'

	try:
		obj = LadiesSkirt.objects.get(id=id)
	except LadiesSkirt.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = LadiesSkirtForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = LadiesSkirtForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def ladies_skirt_print_view(request, id):
	template = 'ladies/skirt/ladies_skirt_print.html'

	try:
		obj = LadiesSkirt.objects.get(id=id)
	except LadiesSkirt.DoesNotExist:
		raise Http404

	context = {
		'object': obj,
	}

	return render(request, template, context)


def ladies_tshirt_view(request, id):
	template = 'ladies/t-shirt/ladies_tshirt.html'

	try:
		obj = LadiesTshirt.objects.get(id=id)
	except LadiesTshirt.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = LadiesTshirtForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = LadiesTshirtForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def ladies_tshirt_print_view(request, id):
	template = 'ladies/t-shirt/ladies_tshirt_print.html'

	try:
		obj = LadiesTshirt.objects.get(id=id)
	except LadiesTshirt.DoesNotExist:
		raise Http404

	context = {
		'object': obj,
	}

	return render(request, template, context)


def maternity_frock_view(request, id):
	template = 'ladies/maternity-frock/maternity_frock.html'

	try:
		obj = MaternityFrock.objects.get(id=id)
	except MaternityFrock.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = MaternityFrockForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = MaternityFrockForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def maternity_frock_print_view(request, id):
	template = 'ladies/maternity-frock/maternity_frock_print.html'

	try:
		obj = MaternityFrock.objects.get(id=id)
	except MaternityFrock.DoesNotExist:
		raise Http404

	context = {
		'object': obj,
	}

	return render(request, template, context)


def kaftan_view(request, id):
	template = 'ladies/kaftan/kaftan.html'

	try:
		obj = Kaftan.objects.get(id=id)
	except Kaftan.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = KaftanForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = KaftanForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def kaftan_print_view(request, id):
	template = 'ladies/kaftan/kaftan_print.html'

	try:
		obj = Kaftan.objects.get(id=id)
	except Kaftan.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}

	return render(request, template, context)


def nightwear_view(request, id):
	template = 'ladies/nightwear/nightwear.html'

	try:
		obj = Nightwear.objects.get(id=id)
	except Nightwear.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = NightwearForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = NightwearForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def nightwear_print_view(request, id):
	template = 'ladies/nightwear/nightwear_print.html'

	try:
		obj = Nightwear.objects.get(id=id)
	except Nightwear.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}

	return render(request, template, context)


def boys_pant_view(request, id):
	template = 'boys/pant/boys_pant.html'

	try:
		obj = BoysPant.objects.get(id=id)
	except BoysPant.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = BoysPantForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = BoysPantForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def boys_pant_print_view(request, id):
	template = 'boys/pant/boys_pant_print.html'

	try:
		obj = BoysPant.objects.get(id=id)
	except BoysPant.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}

	return render(request, template, context)


def boys_shirt_view(request, id):
	template = 'boys/shirt/boys_shirt.html'

	try:
		obj = BoysShirt.objects.get(id=id)
	except BoysShirt.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = BoysShirtForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = BoysShirtForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def boys_shirt_print_view(request, id):
	template = 'boys/shirt/boys_shirt_print.html'

	try:
		obj = BoysShirt.objects.get(id=id)
	except BoysShirt.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}

	return render(request, template, context)


def boys_tshirt_view(request, id):
	template = 'boys/t-shirt/boys_tshirt.html'

	try:
		obj = BoysTshirt.objects.get(id=id)
	except BoysTshirt.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = BoysTshirtForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = BoysTshirtForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def boys_tshirt_print_view(request, id):
	template = 'boys/shirt/boys_shirt_print.html'

	try:
		obj = BoysTshirt.objects.get(id=id)
	except BoysTshirt.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}

	return render(request, template, context)


def boys_short_view(request, id):
	template = 'boys/short/boys_short.html'

	try:
		obj = BoysShort.objects.get(id=id)
	except BoysShort.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = BoysShortForm(data=request.POST, instance=obj)
		if form.is_valid():
			form.save()
	else:
		form = BoysShortForm(instance=obj)

	context = {
		'object': obj,
		'form': form,
	}

	return render(request, template, context)


def boys_short_print_view(request, id):
	template = 'boys/short/boys_short_print.html'

	try:
		obj = BoysShort.objects.get(id=id)
	except BoysShortForm.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}

	return render(request, template, context)

