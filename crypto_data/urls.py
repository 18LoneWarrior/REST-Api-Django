from django.urls import path, include
from .views import BlockChainView, CryptoView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Registering router for viewset
router = DefaultRouter()
# Registering BlockChainView and CryptoView with router
router.register('chaindata', BlockChainView, basename='blockchain')
router.register('cryptodata', CryptoView, basename='cryptodata')

urlpatterns = [
    path('', include(router.urls)),                                            # Registers the router urls
    path('access/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Access token urls for JWT
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),        # refresh token urls for JWT
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),           # verify token urls for JWT
]
