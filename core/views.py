from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from payments.models import EthereumTransaction, FlaggedTransaction, SuspiciousAddresses

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def IndexView(request):
    return HttpResponseRedirect('/dashboard/')

@login_required(login_url=settings.LOGIN_URL)
def Dashboard(request):
    total_transactions_loaded = EthereumTransaction.objects.all().count()
    checked_transactions = EthereumTransaction.objects.filter(is_checked=True)
    latest_suspicious_addresses = SuspiciousAddresses.objects.all().order_by('-id')[:10]

    context = {
        'total_transactions_loaded': total_transactions_loaded,
        'checked_transactions_count': checked_transactions.count(),
        'flagged_transactions_count': FlaggedTransaction.objects.all().count(),
        'suspicious_addresses_count': SuspiciousAddresses.objects.all().count(),
        'latest_suspicious_addresses': latest_suspicious_addresses,
        'flagged_transactions': FlaggedTransaction.objects.all().order_by('-id')[:10],
    }

    return render(request, 'dashboard.html', context)