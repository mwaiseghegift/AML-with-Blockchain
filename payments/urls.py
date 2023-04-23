from django.urls import path
from .views import transaction_list

app_name = 'payments'

urlpatterns = [
    path('transactions/', transaction_list, name='transactions'),
]