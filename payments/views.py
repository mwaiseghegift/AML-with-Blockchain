# views.py (modified)

from django.shortcuts import render
from .models import EthereumTransaction
from .utils import get_latest_transactions

def transaction_list(request):
    transactions = get_latest_transactions()
    return render(request, 'transaction_list.html', {'transactions': transactions})


def transactions(request):
    transactions = EthereumTransaction.objects.order_by('-timestamp')

    context = {
        'transactions': transactions
    }

    return render(request, 'transactions.html', context)
