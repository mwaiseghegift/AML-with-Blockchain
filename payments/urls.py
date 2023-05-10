from django.urls import path
from .views import *

app_name = 'payments'

urlpatterns = [
    path('load-transactions/', transaction_list, name='transactions'),
    path('transactions-list/', transactions, name='transactions-list'),
    path('latest-reports/', latest_reports, name='latest-reports'),

]