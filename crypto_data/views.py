from rest_framework import viewsets
from .models import Crypto, BlockChain
from .serializers import CryptoSerializer, BlockSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class BlockChainView(viewsets.ModelViewSet):
    queryset = BlockChain.objects.all()
    serializer_class = BlockSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['^blockchain', '^symbol']


class CryptoView(viewsets.ModelViewSet):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['^currency', '^symbol']
