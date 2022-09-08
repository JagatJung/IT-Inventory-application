"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('20000209/', admin.site.urls),
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    #=================================
    path('venderSubmit/', views.addVendor, name='addVendorData'),
    path('records/', views.DataDashboard, name='Data records'),
    path('delete_vendor/', views.Delete_Vendors, name='Data deletion'),
    path('venderEdit/', views.venderEdit, name='Data edit'),
   
   #=======================================
    path('devicetypeSubmit/', views.devicetypeSubmit, name='Submitting device type'),
    path('deviceSubmit/', views.deviceSubmit, name='Submitting device'),
    path('deviceShow/', views.deviceShow, name='device data tables'),
    path('delete_device/', views.deldevices, name='device delete'),
    path('deviceEdit/', views.deviceEdit, name='device editing'),
    
    #=============================
    path('registeruser/', views.registeruser, name='insterting the users'),
    path('employeeShow/', views.employeeShow, name='data table of the users'),
    path('delete_Employee/', views.delete_Employee, name='data table of the users'),
    path('edit_Employee/', views.edit_Employee, name='data table of the users'),

    #==========================================
    path('registerissue/', views.registerissue, name='registering the issues'),
    path('showIssue/', views.showIssue, name='showing issues'),
    path('delete_issue/', views.deleteIssue, name='showing issues'),
]
