from rest_framework import serializers
from .models import Auction, Bid
from datetime import datetime
from django.utils.timezone import now

#Serializer for auctions objects, confirms the submitted object meets the relevant 
#criteria for the object. 
class AuctionSerializer(serializers.ModelSerializer):

    def validate_description(self, description):
        if len(description) > 255:
            return False
        return True

    #Adds a new bid to the auction if it is higher than the current bid and if the 
    # bidder is not the auction owner. 
    def bid_update(self, instance, bid):
        if bid.user == instance.owner:
            return False, "You cannot bid on your own auctions"
        elif instance.end_time < now:
            return False, "You cannot bid on an expired auction"
        elif bid.amount > instance.highest_bid_amount:
            instance.highest_bid = bid
            instance.highest_bid_amount = bid.amount
            instance.save()
            return True, instance
        else:
            return False, "You must bid higher than the current max bid"

    class Meta:
        model = Auction
        fields = ['id',
            'owner',
            'description',
            'highest_bid',
            'highest_bid_amount', 
            'winner',
            'end_time']
        extra_kwargs={'highest_bid': {'required': False}}
        

#Bid serializer, makes sure that the bid is valid. 
class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = [
            'id',
            'auction',
            'amount',
            'user']