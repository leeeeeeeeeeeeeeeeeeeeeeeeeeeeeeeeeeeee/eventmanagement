"""
URL configuration for eventmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from event import views

urlpatterns = [
    path('strt/',views.strt),
    path('home/',views.home),
    path('packages/',views.packages),
    path('signpage/',views.signpage),
    path('clienthome/',views.clienthome),
   
    path('cprofile/',views.cprofile),
    path('editcprfle/',views.editcprfle),
    path('cpedited/',views.cpedited),
    path('cpass/', views.cpass),
    path('adminhm/', views.adminhm),
    path('cpasscahnge/', views.cpasscahnge),
    path('feed/', views.feed),
    path('feedbacks/', views.feedbacks),
    path('addpkg/', views.addpkg),
    path('request/', views.request),
    path('v_reject/<cid>', views.v_reject),
    path('v_accept/<cid>', views.v_accept),
    path('edelete/<cid>', views.edelete),
    path('chome/', views.chome),
    path('e_edit/', views.e_edit),
    path('e_editpage/<cid>', views.e_editpage),
    path('showmore/<cid>', views.showmore),
    path('accept_appointment/', views.accept_appointment),
    path('reject_appointment/<cid>', views.reject_appointment),
    path('ajxbooking/', views.ajxbooking),
    path('complntpage/', views.complntpage),
    path('sendcomplaint/', views.sendcomplaint),
    path('admincomplaint/', views.admincomplaint),
    path('adminreply/', views.adminreply),
    path('adminfeedback/', views.adminfeedback),
    path('shwrequsts/<cid>', views.shwrequsts),
    path('estiamteaccept/<cid>', views.estiamteaccept),
    path('estimatereject/<cid>', views.estimatereject),
    path('openevent/<id>', views.openevent),
    path('raz_pay/<amount>/<id>', views.raz_pay),
    path('loginpage/', views.loginpage),
    path('make_enquery/<cid>', views.make_enquery),
    path('equiriespage/', views.equiriespage),


    # path('paymentpage/<cid>', views.paymentpage),
]
