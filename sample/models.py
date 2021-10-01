from django.db import models

# Create your models here.

from accessories.models import *
from fabric.models import *


# Ladies

class LadiesFrock(models.Model):
    img = models.ImageField(upload_to='products/ladies/ladies-frock/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    accessories = models.ForeignKey(AccSentOut, on_delete=models.SET_NULL, null=True, blank=True)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class LadiesBlouse(models.Model):
    img = models.ImageField(upload_to='products/ladies/ladies-blouse/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no

class LadiesSkirt(models.Model):
    img = models.ImageField(upload_to='products/ladies/ladies-skirt/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class LadiesPant(models.Model):
    img = models.ImageField(upload_to='products/ladies/ladies-pant/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class MaternityFrock(models.Model):
    img = models.ImageField(upload_to='products/ladies/maternity-frock/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class Kaftan(models.Model):
    img = models.ImageField(upload_to='products/ladies/kaftan/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class LadiesTshirt(models.Model):
    img = models.ImageField(upload_to='products/ladies/ladies-tshirt/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class Nightwear(models.Model):
    img = models.ImageField(upload_to='products/ladies/nightwear/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no

# Childrens
class ChildrensFrock(models.Model):
    img = models.ImageField(upload_to='products/childrens/childrens-frock/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class ChildrensPant(models.Model):
    img = models.ImageField(upload_to='products/childrens/childrens-pant/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


# Infant
class InfantsFrock(models.Model):
    img = models.ImageField(upload_to='products/infants/infants-frock/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class InfantsPant(models.Model):
    img = models.ImageField(upload_to='products/infants/infants-pant/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


# Girls
class GirlsFrock(models.Model):
    img = models.ImageField(upload_to='products/girls/girls-frock/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class GirlsPant(models.Model):
    img = models.ImageField(upload_to='products/girls/girls-pant/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class GirlsTshirt(models.Model):
    img = models.ImageField(upload_to='products/girls/girls-tshirt/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class GirlsShort(models.Model):
    img = models.ImageField(upload_to='products/girls/girls-short/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


# Boys
class BoysPant(models.Model):
    img = models.ImageField(upload_to='products/boys/boys-pant/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.style_no)


class BoysShirt(models.Model):
    img = models.ImageField(upload_to='products/boys/boys-shirt/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class BoysTshirt(models.Model):
    img = models.ImageField(upload_to='products/boys/boys-tshirt/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


class BoysShort(models.Model):
    img = models.ImageField(upload_to='products/boys/boys-short/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no


# Teen
class Teenfrock(models.Model):
    img = models.ImageField(upload_to='products/teen/teen-frock/img/')
    sample_manufactured_date = models.DateField()
    style_no = models.CharField(max_length=1000)
    fabric = models.ForeignKey(OrderOut, on_delete=models.SET_NULL, null=True, blank=True)
    fabric_price = models.DecimalField(decimal_places=2, max_digits=100000)
    consumption = models.CharField(max_length=1000)
    acc_name = models.CharField(max_length=1000)
    acc_id = models.CharField(max_length=1000)
    acc_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    sewing_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    embroidery_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    washed_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    paint_cost = models.DecimalField(decimal_places=2, max_digits=100000)
    factory_profit = models.DecimalField(decimal_places=2, max_digits=100000)
    total_value = models.DecimalField(decimal_places=2, max_digits=100000)
    accepted = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.style_no