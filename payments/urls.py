from django.urls import path
from .views import *

app_name = 'payments'

urlpatterns = [
    path('transactions/', transaction_list, name='transactions'),
    path('transactions-list/', transactions, name='transactions-list'),

]