from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from .forms import add
from .models import product as data
from user.models import cart
# Create your views here.
def addproduct(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = add(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('/product/add/')
			else:
				print (form.errors)
				return redirect('/')
		else:
			form = add()
			context = {'form': form}
			return render(request, 'add_product.html', context)
	else:
		return redirect('/')

def shop(request):
	if request.method == "POST":
		pid = request.POST.get('pid')
		quantity = request.POST.get('quantity')
		temp = data.objects.get(id=pid)
		u=request.user
		c = cart(product=temp, user=u, quantity=quantity)
		c.save()
		return redirect('/product/shop/')
	else:
		p = data.objects.all()
		return render(request, "shop.html", {'p':p})

	