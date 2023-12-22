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

app_name = 'sales'

urlpatterns = [
path('create_account/',views.signup, name='signup'),
path('index/', views.index, name='index'),
path('loginpage/', views.lgn, name='index_login'),
path('employee/dashboard/',views.dashboard, name='dashboard'),
path('employee/messages/',views.msgs, name='messages'),
path('employee/messages/websitequery',views.msgs_wq, name='webiste_query'),
path('employee/messages/colleague',views.msgs_cg, name='colleague'),
path('employee/messages/head-office',views.msgs_bs, name='headoffice'),
path('employee/updates/',views.imptudts, name='updates'),
path('employee/offers/',views.offers, name='offers'),
path('manager/dashboard/',views.md_dashboard, name='dashboard'),
# path('manager/messages/',views.md_msgs, name='dashboard'),
path('booking/mobileservice',views.msbkg, name='msbkg'),
path('booking/computerservice',views.csbkg, name='csbkg'),
path('booking/otherapplianceservice',views.oasbkg, name='oasbkg'),
path('invoice', views.invoice, name='invoice'),
path('employee/logout', views.lgtpg, name='logout')
]
