from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from user.models import order

def home(request):
	return render(request, "home.html", {})

def signout(request):
	auth.logout(request)
	return redirect('/')

def about(request):
	return render(request, "about.html", {})

def orderplaced(request):
	return render(request, "order_placed.html", {})

def orders(request):
	o = order.objects.all()
	return render(request, "orders.html", {'orders':o})

def confirmorder(request):
	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order.objects.get(id=cId)

		tt.status = "Dispatched"
		tt.save()
		return redirect('/orders/')

	else:
		return redirect('/orders/')

def delivered(request):
	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order.objects.get(id=cId)

		tt.status = "Delivered"
		tt.save()
		return redirect('/orders/')

	else:
		return redirect('/orders/')

def confirmpay(request):
	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order.objects.get(id=cId)

		tt.paid = "True"
		tt.save()
		return redirect('/orders/')

	else:
		return redirect('/orders/')

def cancelorder(request):
	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order.objects.get(id=cId)

		tt.status = "Cancelled"
		tt.save()
		return redirect('/user/history')

	else:
		return redirect('/user/history')