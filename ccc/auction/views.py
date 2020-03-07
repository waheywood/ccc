from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Auction, Bid
from .serializers import AuctionSerializer, BidSerializer
# Create your views here.

class AuctionViewSet(viewsets.ModelViewSet):

    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

    def create(self, request):
        s = AuctionSerializer(data=request.data)
        if s.is_valid():
            s.save(owner=request.user)
            return Response(s.data,
                status=status.HTTP_201_CREATED)
        return Response("Invalid arguments: %s" % s.errors,
            status=status.HTTP_400_BAD_REQUEST)

        


class BidViewSet(viewsets.ModelViewSet):

    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def create(self, request):
        s = BidSerializer(data=request.data)
        auction = get_object_or_404(Auction, pk=request.POST["auction"])
        a = AuctionSerializer(data=auction)
        if s.is_valid():
            bid = s.save(user=request.user)
            err, value = a.bid_update(auction, bid)
            if err:                    
                return Response(s.data,
                    status=status.HTTP_201_CREATED)
            else:
                return Response(value,
                status=status.HTTP_400_BAD_REQUEST)
            
        return Response("Invalid arguments: %s" %s.errors,
            status=status.HTTP_400_BAD_REQUEST)