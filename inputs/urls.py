"""reestr URL Configuration

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
from django.urls import path

from .views import *

urlpatterns = [

    path('ParticularSO/<var>/<var1>',ParticularSO,name='ParticularSO'),

    path('', OPS, name='OPS'),
    path('upload/<shipment_id>',Upload,name='Upload'),

    path('FollowUp/',followupview,name='followupview'),
    path('FollowUpUpdate/<follow_id>/',followupUpdate,name='followupUpdate'),

    path('ClaimCreate/<shipment_id>/', ClaimCreate,name='ClaimCreate'),
    path('ClaimView/<shipment_id>/', ClaimView, name='ClaimView'),
    path('ClaimDelete/<claim_id>/',ClaimDelete, name='ClaimDelete'),
    path('ClaimUpdate/<claim_id>/',ClaimUpdate, name='ClaimUpdate'),

    # path('analisys/',analisys,name='analisys')
    path('CreateBuffer/', CreateBuffer, name='CreateBuffer'),

    path('buffer/<shipment_id>',buffer,name='buffer'),
    path('comment/<buffer_id>', comment, name='comment'),
    path('DelBuffer/<buffer_id>', DelBuffer, name='DelBuffer'),

    path('Away/<away>/',Away,name='Away'),
    path('Particular/<var>/<var1>/',Particular,name='Particular'),
    path('AwailableSO/<purchaise_id>/', AwailableSO, name='AwailableSO'),
    path('Overload/<purchaise_id>/<sales_id>/', Overload, name='Overload'),

    path('Allocate/<purchaise_id>,<sale_id>/', Allocate, name='Allocate'),

    path('Login',LogIn.as_view(), name='LoginView'),
    path('Spot/<readiness_id>',Spot, name='Spot'),

    path('SalesCreate/', SalesCreate, name='SalesCreate'),
    path('SalesUpdate/<sales_id>/', SalesUpdate, name = 'SalesUpdate'),
    path('SalesUpdate1/<sales_id>/', SalesUpdate1, name='SalesUpdate1'),
    path('SalesDelete/<sales_id>/', SalesDelete, name='SalesDelete'),
    path('SalesDelete1/<sales_id>/', SalesDelete1, name='SalesDelete1'),
    path('SalesViews/', SalesViews, name='SalesViews'),

    path('PurchaisesCreate/', PurchaisesCreate, name = 'PurchaisesCreate'),
    path('PurchaisesViews/<sales_id>/', PurchaisesViews, name = 'PurchaisesViews'),
    path('PurchaisesViews1/<sales_id>/', PurchaisesViews1, name='PurchaisesViews1'),

    path('PurchaisesUpdate/<purchaise_id>',PurchaisesUpdate, name='PurchaisesUpdate'),
    path('PurchaiseDelete/<purchaise_id>/', PurchaisesDelete, name='PurchaisesDelete'),

    path('ShipmentUpdate/<shipment_id>', ShipmentUpdate, name='ShipmentUpdate'),
    path('ShipmentUpdate1/<shipment_id>', ShipmentUpdate1, name='ShipmentUpdate1'),

    path('ShipmentDelete/<shipment_id>/', ShipmentDelete, name='ShipmentDelete'),
    path('ShipmentDelete1/<shipment_id>/', ShipmentDelete1, name='ShipmentDelete1'),

    path('ShipmentDetail/<shipment_id>/', ShipmentDetail, name='ShipmentDetail'),
    path('ShipmentView/<purchaise_id>/', ShipmentView, name='ShipmentView'),
    path('ShipmentView1/<purchaise_id>/', ShipmentView1, name='ShipmentView1'),

    path('ContainerCreate/<shipment_id>/', ContainerCreate, name='ContainerCreate'),
    path('ContainerCreate1/<shipment_id>/', ContainerCreate1, name='ContainerCreate1'),

    path('ContainerUpdate/<container_id>/', ContainerUpdate, name='ContainerUpdate'),
    path('ContainerUpdate1/<container_id>/', ContainerUpdate1, name='ContainerUpdate1'),


    path('ContainerDelete/<container_id>/', ContainerDelete, name='ContainerDelete'),
    path('ContainerDelete1/<container_id>/', ContainerDelete1, name='ContainerDelete1'),

    path('ContainerViews/<shipment_id>/', ContainerViews, name='ContainerViews'),
    path('Container/<shipment_id>/', Container, name='Container'),

    path('FreightCreate/', FreightCreate, name='FreightCreate'),
    path('FreightUpdate/<freight_id>/', FreightUpdate, name='FreightUpdate'),
    path('FreightDelete/<freight_id>/', FreightDelete, name='FreightDelete'),
    path('FreightViews/<POL>/<POD>/', FreightViews, name='FreightViews'),
    path('FreightSearch/', renewfreight, name='FreightSearch'),

    path('CostViews/<shipment_id>/', CostViews, name='CostViews'),
    path('CostCreate/<shipment_id>/', CostCreate, name='CostCreate'),
    path('CostCreate1/<shipment_id>/', CostCreate1, name='CostCreate1'),

    path('CostsDelete/<cost_id>/', CostDelete, name='CostsDelete'),
    path('CostsDelete1/<cost_id>/', CostDelete1, name='CostsDelete1'),

    path('Costs/<shipment_id>/', Cost, name='Cost'),
    path('C/<shipment_id>/', C, name='C'),

    path('CostMonthlyView/<monthly_id>/', CostMonthlyView, name='CostMonthlyView'),
    path('CostMonthlyCreate/<monthly_id>/', CostMonthlyCreate, name='CostMonthlyCreate'),
    path('CostMonthlyDelete/<cost_id>/', CostMonthlyDelete, name='CostMonthlyDelete'),

    path('MonthlyCreate/<monthly_id>/', MonthlyCreate, name='MonthlyCreate'),

    path('CostMonthlyView1/<monthly_id>/', CostMonthlyView1, name='CostMonthlyView1'),
    path('CostMonthlyCreate1/<monthly_id>/', CostMonthlyCreate1, name='CostMonthlyCreate1'),
    path('CostMonthlyDelete1/<cost_id>/', CostMonthlyDelete1, name='CostMonthlyDelete1'),

    path('FinCostMonthlyView/<monthly_id>/', FinCostMonthlyView, name='FinCostMonthlyView'),
    path('FinCostMonthlyCreate/<monthly_id>/', FinCostMonthlyCreate, name='FinCostMonthlyCreate'),
    path('FinCostMonthlyDelete/<cost_id>/', FinCostMonthlyDelete, name='FinCostMonthlyDelete'),

    path('FinCostMonthlyView1/<monthly_id>/', FinCostMonthlyView1, name='FinCostMonthlyView1'),
    path('FinCostMonthlyCreate1/<monthly_id>/', FinCostMonthlyCreate1, name='FinCostMonthlyCreate1'),
    path('FinCostMonthlyDelete1/<cost_id>/', FinCostMonthlyDelete1, name='FinCostMonthlyDelete1'),

    path('ShowFreight/<readiness_id>/', ShowFreight, name='ShowFreight'),
    path('Select/<freight_id>/<readiness_id>/', Select, name='Select'),
    path('Skip/<readiness_id>/', Skip, name='Skip'),

    path('Search', Search, name='Search'),
    path('Result/<number>/', Result, name='Result'),

    path('Report', report, name='Report'),
    path('cunter',reportcounter,name='counter'),
    path('reportOrders', reportOrders, name='reportOrders'),
    path('reportClaims', reportClaims, name='reportClaims'),
    path('reportClaimsUA', reportClaimsUA, name='reportClaimsUA'),

    path('Monthly/<shipment_id>', MonthlyReports, name='Monthly'),
    path('Monthly1/<shipment_id>', MonthlyReports1, name='Monthly1'),
    path('ReportMonthly/<month>', ReportMonthly, name='ReportMonthly'),

    path('MonthlyView',MonthlyView,name='MonthlyView'),
    path('MonthlyPart/<month>', MonthlyPart, name='MonthlyPart'),

    path('MonthlyUpdate/<monthly_id>',MonthlyUpdate,name='MonthlyUpdate'),
    path('MonthlyUpdate1/<monthly_id>', MonthlyUpdate1, name='MonthlyUpdate1'),
    path('MonthlyDelete/<monthly_id>', MonthlyDelete, name='MonthlyDelete'),
    path('MonthlyDelete1/<monthly_id>', MonthlyDelete1, name='MonthlyDelete1'),

    path('ReadinessUpdate/<read_id>/', ReadinessUpdate, name='ReadinessUpdate'),
    path('Split/<read_id>', Split, name='Split'),
    path('Delete/<read_id>', ReadinessDelete, name='Delete'),

    path('Close/<sales_id>', Close, name='Close'),
    path('Close1/<sales_id>', Close1, name='Close1'),
    path('Open/<sales_id>', Open, name='Open'),
    # path('Move/<purchaise_id>', Move, name='Move'),
]
