# views.py (modified)

from django.shortcuts import render
from .models import EthereumTransaction
from .utils import get_latest_transactions, deploy_anti_money_laundering_contract
from django.core.paginator import Paginator

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
