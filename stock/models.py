from django.db import models

from django.contrib.auth.models import User
from sample.models import *
from orders.models import OrderReceiving
from customers.models import Customer


# Create your models here.
class LadiesFrockStock(models.Model):
    date = models.DateField()
    order_received = models.DateField()
    sample = models.ForeignKey(LadiesFrock, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(OrderReceiving, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.CharField(max_length=20000)
    damage = models.BooleanField(default=False)
    accepted = models.BooleanField(default=True)
    quantity = models.IntegerField()
    balance_quantity = models.IntegerField()
    delivery_date = models.DateField()
    order_delivered = models.BooleanField(default=True)
    delivered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()



