from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("Response.")

class Auction(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Getting auction %s" % kwargs["auctionID"])

class User(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Getting user %s" % kwargs["userID"])