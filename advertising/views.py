from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Advertiser, Ad, Location, Transaction
from .serializers import AdvertiserSerializer, AdSerializer, LocationSerializer, TransactionSerializer


# Create your views here.

class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    @action(detail=False, methods=['get'])
    def ad_spend_location(self, request, *args, **kwargs):
        location = request.query_params.get('location')
        if not location:
            return Response({'detail': 'location query parameter is required...'}, status=400)

        total_ad_spend = Ad.objects.filter(location__name=location).aggregate(total_spend=Sum('spend'))
        return Response({'total_ad_spend': total_ad_spend})


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
