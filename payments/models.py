# models.py

from django.db import models

class EthereumTransaction(models.Model):
    sender = models.CharField(max_length=42)
    receiver = models.CharField(max_length=42)
    value = models.FloatField()
    gas_price = models.FloatField(blank=True, null=True)
    gas_used = models.FloatField(blank=True, null=True)
    block_number = models.IntegerField(blank=True, null=True)
    transaction_fee = models.FloatField(blank=True, null=True)
    is_contract_creation = models.BooleanField(default=False)
    eth_timestamp = models.CharField(max_length=42, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'ethereum_transactions'
        

    def __str__(self):
        return f'{self.sender} sent {self.value} ETH to {self.receiver} at {self.timestamp}'

