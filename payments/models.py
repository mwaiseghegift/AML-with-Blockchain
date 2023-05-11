# models.py

from django.db import models

FLAGGED_REASON = (
    ('1', 'Suspicious Amount'),
    ('2', 'Suspicious Receiver'),
    ('3', 'Suspicious Sender'),
    ('4', 'Suspicious Gas Price'),
    ('5', 'Suspicious Gas Used'),
    ('6', 'Suspicious Transaction Fee'),
    ('7', 'Suspicious Timestamp'),
    ('8', 'Suspicious Block Number'),
    ('9', 'Multiple Transactions'),
    ('10', 'Suspicious Contract Creation'),
    ('11', 'Suspicious Transaction Hash'),
    ('12', 'Suspicious Transaction Index'),
    ('13', 'Suspicious Nonce'),
    ('14', 'Suspicious Input'),
)
    

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
    is_checked = models.BooleanField(default=False)
    is_update_checked = models.BooleanField(default=False)

    def get_or_create_frequency(self):
        try:
            address = self.sender
            if AddressFrequency.objects.filter(address=address).exists():
                address_frequency = AddressFrequency.objects.get(address=address)
                address_frequency.times_sender += 1
                address_frequency.save()
            else:
                address_frequency = AddressFrequency.objects.create(address=address, times_sender=1)

            address = self.receiver
            if AddressFrequency.objects.filter(address=address).exists():
                address_frequency = AddressFrequency.objects.get(address=address)
                address_frequency.times_receiver += 1
                address_frequency.save()
            else:
                address_frequency = AddressFrequency.objects.create(address=address, times_receiver=1)
            return address_frequency
        except Exception as e:
            print(e)
            return None

    class Meta:
        ordering = ['-timestamp']
        db_table = 'ethereum_transactions'
        

    def __str__(self):
        return f'{self.sender} sent {self.value} ETH to {self.receiver} at {self.timestamp}'


class FlaggedTransaction(models.Model):
    transaction = models.ForeignKey(EthereumTransaction, on_delete=models.CASCADE)
    sender = models.CharField(max_length=42)
    receiver = models.CharField(max_length=42)
    reason = models.CharField(max_length=50, choices=FLAGGED_REASON)
    is_flagged = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'flagged_transactions'

    def __str__(self):
        return f'{self.transaction} flagged at {self.timestamp}'



class SuspiciousAddresses(models.Model):
    address = models.CharField(max_length=42)
    reason = models.CharField(max_length=50, choices=FLAGGED_REASON)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'suspicious_addresses'


class AddressFrequency(models.Model):
    address = models.CharField(max_length=42)
    times_sender = models.IntegerField(default=0)
    times_receiver = models.IntegerField(default=0)
    last_transaction = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['times_sender', 'times_receiver']
        db_table = 'frequent_addresses'

    def __str__(self):
        return f'{self.address} has been used {self.times_sender} times as sender and {self.times_receiver} times as receiver'


class WhitlistedAddresses(models.Model):
    address = models.CharField(max_length=42)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'whitelisted_addresses'

    def __str__(self):
        return f'{self.address} whitelisted at {self.timestamp}'
    

class BlacklistedAddresses(models.Model):
    address = models.CharField(max_length=42)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'blacklisted_addresses'

    def __str__(self):
        return f'{self.address} blacklisted at {self.timestamp}'
    

class SuspiciousTransactions(models.Model):
    transaction = models.ForeignKey(EthereumTransaction, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50, choices=FLAGGED_REASON)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        db_table = 'suspicious_transactions'

    def __str__(self):
        return f'{self.transaction} is suspicious because {self.reason} at {self.timestamp}'
