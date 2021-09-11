"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mystore.views import home, cancelorder, signout, about, orderplaced, orders, confirmorder, delivered, confirmpay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signout', signout, name='signout'),
    path('orderplaced', orderplaced, name='orderplaced'),
    path('contact/', about, name='contact'),
    path('orders/', orders, name='orders'),
    path('confirmorder', confirmorder, name='confirmorder'),
    path('cancelorder', cancelorder, name='cancelorder'),
    path('confirmpay', confirmpay, name='confirmpay'),
    path('delivered', delivered, name='delivered'),
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
