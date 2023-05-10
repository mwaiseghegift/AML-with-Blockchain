# views.py (modified)

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import EthereumTransaction, FlaggedTransaction, SuspiciousAddresses
from .utils import *
from django.core.paginator import Paginator
import pandas as pd
import joblib


def transaction_list(request):
    transactions = get_latest_transactions()
    
    context = {
        'transactions': transactions,
        
    }
    return render(request, 'transaction_list.html', context)


def transactions(request):
    transactions = EthereumTransaction.objects.order_by('-timestamp')
    # pagination
    paginator = Paginator(transactions, 100)
    page = request.GET.get('page')
    transactions = paginator.get_page(page)

    context = {
        'transactions': transactions,
    }

    return render(request, 'transactions.html', context)



def latest_reports(request):
    flagged_transactions = FlaggedTransaction.objects.order_by('-timestamp')[:20]
    suspicious_addresses = SuspiciousAddresses.objects.order_by('-timestamp')[:20]

    context = {
        'flagged_transactions': flagged_transactions,
        'suspicious_addresses': suspicious_addresses,
    }

    return render(request, 'latest_reports.html', context)


def update_system_reports(request, *args, **kwargs):
    check_transactions()

    # check addresses that have appeared more than 5 times 
    transactions = EthereumTransaction.objects.all(is_update_checked=False)

    for transaction in transactions:
        address_frequency = transaction.get_or_create_frequency()
        if address_frequency:
            if address_frequency.times_sender > 5:
                SuspiciousAddresses.objects.get_or_create(address=transaction.sender, reason='Sender')
            if address_frequency.times_receiver > 5:
                SuspiciousAddresses.objects.get_or_create(address=transaction.receiver, reason='Receiver')

    return HttpResponseRedirect(reverse('core:dashboard'))

    

