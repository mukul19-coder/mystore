from django import forms
from .models import product

class add(forms.ModelForm):
	class Meta:
		model = product
		fields = '__all__'