from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from user.models import profile as data
from user.models import cart as c1
from user.models import order, formatt
import razorpay
# Create your views here.

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		phonenumber = request.POST.get('phonenumber')
		organizationname = request.POST.get('organizationname')
		address = request.POST.get('address')
		gst = request.POST.get('gst')

		u = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
		u.save()
		
		u1 = User.objects.get(email=email)
		p = data(client=u1, phone_number=phonenumber, organization_name=organizationname, address=address, gst=gst)
		p.save()

		return redirect('/')
	else:
		return render(request, "register.html", {})


def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')

		else:
			messages.info(request,'INVALID CREDENTIALS')
			return render(request, "home.html", {})

	else:
		return render(request, "login.html", {})


def profile(request):
	p = data.objects.get(client=request.user.id)
	if request.method == 'POST':
		password = request.POST.get('password')

		u = request.user
		u.set_password(password)
		u.save()
		auth.logout(request)
		return redirect('/user/login')
	else:
		return render(request, "profile.html", {'p':p})


def edit_details(request):
	p = data.objects.get(client=request.user.id)
	return render(request, "edit.html", {'p':p})


def chusername(request):
	uname = request.POST.get('username')
	u = request.user
	u.username = uname
	u.save()
	return redirect('/user/edit_details')

def chemail(request):
	email = request.POST.get('email')
	u = request.user
	u.email = email
	u.save()
	return redirect('/user/edit_details')

def chfirstname(request):
	fname = request.POST.get('firstname')
	u = request.user
	u.first_name = fname
	u.save()
	return redirect('/user/edit_details')

def chlastname(request):
	lname = request.POST.get('lastname')
	u = request.user
	u.last_name = lname
	u.save()
	return redirect('/user/edit_details')

def chaddress(request):
	address = request.POST.get('address')
	p = data.objects.get(user=request.user.id)
	p.address = address
	p.save()
	return redirect('/user/edit_details')

def chphonenumber(request):
	phonenumber = request.POST.get('phonenumber')
	p = data.objects.get(user=request.user.id)
	p.phone_number = phonenumber
	p.save()
	return redirect('/user/edit_details')

def chorganizationname(request):
	organizationname = request.POST.get('organizationname')
	p = data.objects.get(user=request.user.id)
	p.organization_name = organizationname
	p.save()
	return redirect('/user/edit_details')

def chgst(request):
	gst = request.POST.get('gst')
	p = data.objects.get(user=request.user.id)
	p.gst = gst
	p.save()
	return redirect('/user/edit_details')


def cart(request):
	c = c1.objects.filter(user=request.user)
	w=0
	for t in c:
		temp = float(t.quantity) * float(t.product.price)
		w=w + temp

	return render(request, "cart.html", {'cart':c, 'total':w})

def deleteitem(request):
	i = request.POST.get('pid')
	c = c1.objects.get(id=i)
	c.delete()
	return redirect('/user/cart')

def payment(request):
	c = c1.objects.filter(user=request.user)
	w=0
	for t in c:
		temp = float(t.quantity) * float(t.product.price)
		w=w + temp

	if request.method == "POST":
		pay = request.POST.get('payment')
		if pay == "op":
			a = w * 100
			
			keyid = 'rzp_test_dAGXWujcJfTtay'
			keySecret = 'l2QsVhXh0CgYd0CTAWLfEdqj'
			client = razorpay.Client(auth=(keyid, keySecret))
			payment = client.order.create({'amount': a, 'currency':'INR', 'payment_capture': '1'})

			f = formatt.objects.get(id=1)
			t1 = int(f.number)
			f1 = t1 + 1
			f2 = "%s" %f1
			f3 = f2.zfill(3)
			f.number = f3
			f.save()

			u = request.user
			for t in c:
				o = order(product=t.product, user=u, quantity=t.quantity, paymethod="Online Payment", totalamount=w, invoice_no=f3, payment_id=payment['id'], paid="True")
				o.save()

			return render(request, "payment.html", {'cart':c, 'total':w, 'payment':payment})
		else:
			f = formatt.objects.get(id=1)
			t1 = int(f.number)
			f1 = t1 + 1
			f2 = "%s" %f1
			f3 = f2.zfill(3)
			f.number = f3
			f.save()

			u = request.user
			for t in c:
				o = order(product=t.product, user=u, quantity=t.quantity, paymethod="Cash On Delivery", totalamount=w, invoice_no=f3, payment_id="COD")
				o.save()

			c.delete()
			return redirect('/orderplaced')
	else:	
		return render(request, "payment.html", {'cart':c, 'total':w})

def success(request):
	c = c1.objects.filter(user=request.user)
	f = formatt.objects.get(id=1)
	o = order.objects.filter(invoice_no=f)
	w=0
	for t in c:
		temp = float(t.quantity) * float(t.product.price)
		w=w + temp

	if request.method == "POST":
		a = request.POST

		c.delete()
		return render(request, 'success.html', {'pay':a, 'total':w})

def history(request):
	o = order.objects.filter(user=request.user)
	return render(request, "history.html", {'orders':o})

def details(request):
	ino = request.POST.get('invoicenumber')
	o = order.objects.filter(invoice_no=ino)
	return render(request, "history_details.html", {'orders':o})
