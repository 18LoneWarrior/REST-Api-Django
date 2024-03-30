from django.contrib import admin
from .models import BlockChain, Crypto


@admin.register(BlockChain)
class BlockChainAdmin(admin.ModelAdmin):
    list_display = ['id', 'blockchain']


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ['id', 'blockchain', 'currency', 'symbol', 'price', 'market_cap']
