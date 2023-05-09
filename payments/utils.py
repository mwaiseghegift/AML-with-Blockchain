# utils.py

from web3 import Web3
from .models import EthereumTransaction
from django.conf import settings

w3 = Web3(Web3.HTTPProvider(settings.ETHEREUM_NODE_URL))

def get_latest_transactions():
    # Connect to Ethereum network using an Ethereum node URL
    w3 = Web3(Web3.HTTPProvider(settings.ETHEREUM_NODE_URL))

    # Retrieve the latest 10 Ethereum transactions
    # request the latest block number
    ending_blocknumber = w3.eth.get_block('latest').number

    blocks = 50

    transactions = []
    # Retrieve the transactions for each block
    for block_number in range(ending_blocknumber - blocks, ending_blocknumber):
        block = w3.eth.get_block(block_number)
        for transaction in block.transactions:
            tx = w3.eth.get_transaction(transaction.hex())
            sender = tx['from']
            receiver = tx['to']
            value = w3.from_wei(tx['value'], 'ether')
            timestamp = w3.eth.get_block(block_number)['timestamp']
            try:
                EthereumTransaction.objects.create(
                    sender=sender,
                    receiver=receiver,
                    value=value,
                    timestamp=timestamp,
                )
            except:
                pass
            transactions.append({
                'sender': sender,
                'receiver': receiver,
                'value': value,
                'timestamp': timestamp,
            })

    # Return the transactions
    return transactions

# utils.py (continued)
from .contracts import ANTI_MONEY_LAUNDERING_ABI, ANTI_MONEY_LAUNDERING_BYTECODE

w3 = Web3(Web3.HTTPProvider(settings.ETHEREUM_NODE_URL))

def deploy_anti_money_laundering_contract():
    account = w3.eth.account.create()
    contract = w3.eth.contract(abi=ANTI_MONEY_LAUNDERING_ABI, bytecode=ANTI_MONEY_LAUNDERING_BYTECODE)
    tx_hash = contract.constructor().transact({
        'from': account.address,
        'gas': 1000000,
    })
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    contract_address = tx_receipt.contractAddress
    return contract_address
