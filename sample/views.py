from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.


"""def sample_main_view(request):

	return render(request, 'sample_main.html', {})"""


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

			# Boys
			'boys_pants': self.get_boys_pant_queryset(),
			'boys_shirts': self.get_boys_shirt_queryset(),
			'boys_tshirts': self.get_boys_tshirt_queryset(),
			'boys_shorts': self.get_boys_short_queryset(),

			# Girls
			'girls_frocks': self.get_girls_frock_queryset(),
			'girls_pants': self.get_girls_pant_queryset(),
			'girls_tshirts': self.get_girls_tshirt_queryset(),
			'girls_shorts': self.get_girls_short_queryset(),

			# Infants
			'infants_frocks': self.get_infants_frock_queryset(),
			'infants_pants': self.get_infants_pant_queryset(),

			# Teens
			'teen_frocks': self.get_teen_frock_queryset(),
		}
		return render(request, self.template_name, context)


class LadiesFrockView(View):
	template_name = 'ladies_frock.html'
	queryset = LadiesFrock.objects.all()

	def get_query_set(self):
		return self.queryset

	def get(self, request):
		context = {
			'ladies_frocks': self.get_query_set()
		}

		return render(request, self.template_name, context)
