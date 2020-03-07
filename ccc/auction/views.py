import validators

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Auction, Bid
from .serializers import AuctionSerializer, BidSerializer
# Create your views here.

class AuctionViewSet(viewsets.ModelViewSet):

    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

    def create(self, request):
        form_data = request.POST
        if validators.validate_auction(form_data):
            
            
        


class BidViewSet(viewsets.ModelViewSet):

    queryset = Bid.objects.all()
    serializer_class = BidSerializer