from rest_framework import serializers
from .models import BlockChain, Crypto


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlockChain
        fields = ['id', 'url', 'blockchain', 'symbol']


class CryptoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Crypto
        fields = ['id', 'url', 'blockchain',  'currency', 'symbol', 'price', 'market_cap', 'circulating_supply',
                  'max_supply', 'official_url']
