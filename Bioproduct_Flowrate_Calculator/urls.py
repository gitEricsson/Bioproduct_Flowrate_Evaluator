from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/bioproducts_flowrate_calculator/', include('Flowrate_Calculator.urls')),
]
