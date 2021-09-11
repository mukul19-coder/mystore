from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import login, register, details, payment, history, deleteitem, success, profile, edit_details, chusername, chemail, chfirstname, chlastname, chaddress, chphonenumber, chorganizationname, chgst, cart

urlpatterns = [
    path('login', login, name='login'),
    path('registration', register, name='registration'),
    path('profile', profile, name='profile'),
    path('edit_details', edit_details, name='edit_details'),
    path('chusername', chusername, name='chusername'),
    path('chemail', chemail, name='chemail'),
    path('chfirstname', chfirstname, name='chfirstname'),
    path('chlastname', chlastname, name='chlastname'),
    path('chaddress', chaddress, name='chaddress'),
    path('chphonenumber', chphonenumber, name='chphonenumber'),
    path('chorganizationname', chorganizationname, name='chorganizationname'),
    path('chgst', chgst, name='chgst'),
    path('cart', cart, name='cart'),
    path('deleteitem', deleteitem, name='deleteitem'),
    path('payment', payment, name='payment'),
    path('history', history, name='history'),
    path('success', success, name='success'),
    path('order_details', details, name='details'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
