from django.urls import path
from .views import *

app_name = 'payments'

urlpatterns = [
    path('load-transactions/', transaction_list, name='transactions'),
    path('transactions-list/', transactions, name='transactions-list'),
    path('latest-reports/', latest_reports, name='latest-reports'),
    path('update-system-reports/', update_system_reports, name='update-system-reports'),
    path('top-addresses/', top_addresses, name='top-addresses'),

]