
from django.contrib import admin
from .models import EthereumTransaction

class EthereumTransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'value', 'timestamp')
    list_filter = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender', 'receiver')

admin.site.register(EthereumTransaction, EthereumTransactionAdmin)
