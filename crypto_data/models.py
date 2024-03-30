from django.db import models
import uuid


# Create your models here.

class BlockChain(models.Model):
    BLOCK_CHAIN = (
        ("BITCOIN", "Bitcoin"),
        ("ETHEREUM", "Ethereum"),
        ("SOLANA", "Solana"),
        ("BSC", "BNB"),
        ("MANTA", "Manta"),
        ("POLYGON", "Polygon"),
        ("ARBITRUM", "Arbitrum"),
        ("AVALANCHE", "Avalanche"),
        ("FANTOM", "Fantom"),
        ("HECO", "Heco"),
        ("OKEX", "OKEx"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blockchain = models.CharField(max_length=10, choices=BLOCK_CHAIN, default="ETHEREUM")
    symbol = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.blockchain


class Crypto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blockchain = models.ForeignKey(BlockChain, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    circulating_supply = models.IntegerField()
    max_supply = models.IntegerField()
    official_url = models.URLField(max_length=200)

    def __str__(self):
        return self.currency
