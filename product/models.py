from django.db import models
from django.db.models import Model
from django.db.models import Q
# Create your models here.
class product(models.Model):
	img1 = models.ImageField(upload_to='pics', blank=True)
	name = models.CharField(max_length=100, blank=True)
	desc = models.CharField(max_length=100, blank=True)
	price = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name + " " + self.desc