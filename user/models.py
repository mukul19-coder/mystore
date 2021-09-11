from django.db import models
from django.db.models import Model
from django.db.models import Q
from django.contrib.auth.models import User
from product.models import product as data

# Create your models here.
class profile(models.Model):
	client = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	phone_number = models.CharField(max_length=100, blank=True, default=None)
	organization_name = models.CharField(max_length=100, blank=True, default=None)
	address = models.CharField(max_length=200, blank=True, default=None)
	gst = models.CharField(max_length=100, blank=True, default=None)

	def __str__(self):
		return "For " + self.client.username

class cart(models.Model):
	product = models.ForeignKey(data, on_delete=models.CASCADE, default=None)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	quantity = models.CharField(max_length=100, default=0)

class order(models.Model):
	status = (
		('Order Placed', 'Order Placed'),
		('Dispatched', 'Dispatched'),
		('Delivered', 'Delivered'),
		)
	product = models.ForeignKey(data, on_delete=models.CASCADE, default=None)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	quantity = models.CharField(max_length=100, default=0)
	date  = models.DateField(auto_now_add=True, editable=False)
	paymethod = models.CharField(max_length=100, default="cod")
	totalamount = models.CharField(max_length=100)
	invoice_no = models.CharField(max_length=20, default=None)
	payment_id = models.CharField(max_length=100, default='Cash On Delivery')
	paid = models.BooleanField(default=False)
	status=models.CharField(max_length=100, choices=status, default="Order Placed")

	def __str__(self):
		return "INVOICE " + self.invoice_no + " - " + self.user.username

class formatt(models.Model):
	number = models.CharField(max_length=20)