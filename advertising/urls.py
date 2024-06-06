from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('advertisers', views.AdvertiserViewSet)
router.register('ads', views.AdViewSet)
router.register('locations', views.LocationViewSet)
router.register('transactions', views.TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
