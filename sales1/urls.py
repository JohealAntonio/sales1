"""
URL configuration for sales1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from product_sales import views

urlpatterns = [
path('',views.home,name="home"),
path('signin/',views.signin, name='signin'),
path('signup/',views.signup, name='signup'),
path('profile/',views.profile, name='profile'),
path('home/',views.home, name='home'),
path('homesignin', views.homesignin, name='homesignin'),
path('index/', views.index, name='index'),
path('employee/login/', views.lgn, name='index_login'),
path('employee/dashboard/',views.dashboard, name='dashboard'),
path('employee/messages/',views.msgs, name='messages'),
path('employee/updates/',views.imptudts, name='updates'),
path('employee/offers/',views.offers, name='offers'),
path('booking/mobileservice',views.msbkg, name='msbkg'),
path('booking/computerservice',views.csbkg, name='csbkg'),
path('booking/successpage', views.scspg, name='scspage'),
path('booking/payment', views.paymt, name='bkgpaymt'),
path('invoice', views.invoice, name='invoice'),
]
