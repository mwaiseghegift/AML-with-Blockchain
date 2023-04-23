# utils.py

from web3 import Web3
from .models import EthereumTransaction
from django.conf import settings

def get_latest_transactions():
    # Connect to Ethereum network using an Ethereum node URL
    w3 = Web3(Web3.HTTPProvider(settings.ETHEREUM_NODE_URL))

    # Retrieve the latest 10 Ethereum transactions
    latest_blocks = w3.eth.get_block_numbers(10)
    transactions = []
    # Retrieve the transactions for each block
    for block_number in latest_blocks:
        block = w3.eth.get_block(block_number)
        for transaction in block.transactions:
            tx = w3.eth.get_transaction(transaction.hex())
            sender = tx['from']
            receiver = tx['to']
            value = w3.fromWei(tx['value'], 'ether')
            timestamp = w3.eth.get_block(block_number)['timestamp']
            EthereumTransaction.objects.create(
                sender=sender,
                receiver=receiver,
                value=value,
                timestamp=timestamp,
            )
            transactions.append({
                'sender': sender,
                'receiver': receiver,
                'value': value,
                'timestamp': timestamp,
            })

    # Return the transactions
    return transactions
