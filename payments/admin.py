
from django.contrib import admin
from .models import *

class EthereumTransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'value', 'timestamp')
    list_filter = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender', 'receiver')

admin.site.register(EthereumTransaction, EthereumTransactionAdmin)


@admin.register(FlaggedTransaction)
class FlaggedTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'sender', 'receiver', 'reason', 'is_flagged', 'is_checked', 'timestamp')
    list_filter = ('sender', 'receiver', 'reason', 'is_flagged', 'is_checked', 'timestamp')
    search_fields = ('sender', 'receiver')


@admin.register(SuspiciousAddresses)
class SuspiciousAddressesAdmin(admin.ModelAdmin):
    list_display = ('address', 'reason', 'timestamp')
    list_filter = ('address', 'reason', 'timestamp')
    search_fields = ('address', 'reason')


@admin.register(AddressFrequency)
class AddressFrequencyAdmin(admin.ModelAdmin):
    list_display = ('address', 'times_sender', 'times_receiver')
    list_filter = ('address', 'times_sender', 'times_receiver')
    search_fields = ('address', 'times_sender', 'times_receiver')
