from django.urls import path
from .views import *

app_name = 'payments'

urlpatterns = [
    path('load-transactions/', transaction_list, name='transactions'),
    path('transactions-list/', transactions, name='transactions-list'),
    path('fraud-transactions/', detect_fraud_transactions, name='fraud-transactions'),

]