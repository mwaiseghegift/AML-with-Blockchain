# models.py

from django.db import models

class EthereumTransaction(models.Model):
    sender = models.CharField(max_length=42)
    receiver = models.CharField(max_length=42)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} sent {self.value} ETH to {self.receiver} at {self.timestamp}'

