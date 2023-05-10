# views.py (modified)

from django.shortcuts import render
from .models import EthereumTransaction
from .utils import get_latest_transactions, deploy_anti_money_laundering_contract
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



def detect_fraud_transactions(request):
    # Load the saved model
    with open('finalized_model.sav', 'rb') as f:
        model = pickle.load(f)

    # Get all transactions from the database
    transactions = EthereumTransaction.objects.all()

    # Initialize a list to store the fraud scores for each transaction
    fraud_scores = []

    # Loop over each transaction
    for transaction in transactions:
        # Extract the relevant features from the transaction
        features = [transaction.Avg_min_between_sent_tnx,
                    transaction.Avg_min_between_received_tnx,
                    transaction.Time_Diff_between_first_and_last_Mins,
                    transaction.Sent_tnx,
                    transaction.Received_Tnx,
                    transaction.Number_of_Created_Contracts,
                    transaction.Unique_Received_From_Addresses,
                    transaction.Unique_Sent_To_Addresses,
                    transaction.min_value_received,
                    transaction.max_value_received,
                    transaction.avg_val_received,
                    transaction.min_val_sent,
                    transaction.max_val_sent,
                    transaction.avg_val_sent,
                    transaction.min_value_sent_to_contract,
                    transaction.max_val_sent_to_contract,
                    transaction.avg_value_sent_to_contract,
                    transaction.total_transactions_including_tnx_to_create_contract,
                    transaction.total_Ether_sent,
                    transaction.total_ether_received,
                    transaction.total_ether_sent_contracts,
                    transaction.total_ether_balance,
                    transaction.Total_ERC20_tnxs,
                    transaction.ERC20_total_Ether_received,
                    transaction.ERC20_total_ether_sent,
                    transaction.ERC20_total_Ether_sent_contract,
                    transaction.ERC20_uniq_sent_addr,
                    transaction.ERC20_uniq_rec_addr,
                    transaction.ERC20_uniq_sent_addr_1,
                    transaction.ERC20_uniq_rec_contract_addr,
                    transaction.ERC20_avg_time_between_sent_tnx,
                    transaction.ERC20_avg_time_between_rec_tnx,
                    transaction.ERC20_avg_time_between_rec_2_tnx,
                    transaction.ERC20_avg_time_between_contract_tnx,
                    transaction.ERC20_min_val_rec,
                    transaction.ERC20_max_val_rec,
                    transaction.ERC20_avg_val_rec,
                    transaction.ERC20_min_val_sent,
                    transaction.ERC20_max_val_sent,
                    transaction.ERC20_avg_val_sent,
                    transaction.ERC20_min_val_sent_contract,
                    transaction.ERC20_max_val_sent_contract,
                    transaction.ERC20_avg_val_sent_contract,
                    transaction.ERC20_uniq_sent_token_name,
                    transaction.ERC20_uniq_rec_token_name,
                    transaction.ERC20_most_sent_token_type,
                    transaction.ERC20_most_rec_token_type]

        # Use the model to predict the fraud score for the transaction
        fraud_score = model.predict_proba([features])[0][1]
        fraud_scores.append(fraud_score)

    # Add the fraud scores to the transactions as a new field
    for i, transaction in enumerate(transactions):
        transaction.fraud_score = fraud_scores[i]

    # Order the transactions by their fraud score in descending order
    transactions = sorted(transactions, key=lambda x: x.fraud_score, reverse=True)

    context = {
        'transactions': transactions,
    }

    return render(request, 'flagged_transactions.html', context)