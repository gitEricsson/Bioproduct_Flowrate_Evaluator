from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='Flowrate_Calculator'),
]