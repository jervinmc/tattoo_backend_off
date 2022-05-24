from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,Artist
from tattoo.views import TattooUserID,TattooMarket,TattooMarketArtist
from transaction.views import TransactionUserClientID,TransactionUserArtistID
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#to push

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/tattoo/', include('tattoo.urls')),
    path('api/v1/transaction/', include('transaction.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/tattoo_id/<str:user_id>/', TattooUserID.as_view(), name='get_user'),
    path('api/v1/tattoo_market/', TattooMarket.as_view(), name='get_user'),
    path('api/v1/tattoo_market-artist/<int:user_id>/', TattooMarketArtist.as_view(), name='get_user'),
    path('api/v1/artist/', Artist.as_view(), name='get_user'),
    path('api/v1/transaction_clientid/<str:user_id>/', TransactionUserClientID.as_view(), name='get_user'),
    path('api/v1/transaction_artistid/<str:user_id>/', TransactionUserArtistID.as_view(), name='get_user'),
    path('api/v1/login/', Login.as_view(), name='get_user'),
]