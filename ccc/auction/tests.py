from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import AuctionViewSet, BidViewSet
from .models import  Auction, Bid
from rest_framework import status
from rest_framework.test import APITestCase, APIClient as Client, APIRequestFactory, force_authenticate
import requests

# Create your tests here.



def get_token(user):
    user_token = requests.post('http://localhost:8000/auth/token/', data=user).json()
    return user_token["access_token"]

class UserTest(APITestCase):
    def setUp(self):
        self.mike = {'username': 'mike',
            'password': 'abcdef123',
            'access_token': ''}
        self.mary = {'username': 'mary',
            'password': 'abcdef123',
            'access_token': ''}
        self.oli = {'username': 'oli',
            'password': 'abcdef123',
            'access_token': ''}
        self.client.post('http://localhost:8000/auth/register/', data=self.mike, format='json')
        self.client.post('http://localhost:8000/auth/register/', data=self.mary, format='json')
        self.client.post('http://localhost:8000/auth/register/', data=self.oli, format='json')

    def test_get_tokens(self):
        self.mike["access_token"] = get_token(self.mike)
        self.assertTrue(self.mike["access_token"])
        self.mary["access_token"] = get_token(self.mary)
        self.assertTrue(self.mary["access_token"])
        self.oli["access_token"] = get_token(self.oli)
        self.assertTrue(self.oli["access_token"])

    def test_list_auctions(self):
        self.mike['access_token'] = get_token(self.mike)
        auctions = requests.get('http://localhost:8000/api/auction/', data=self.mike)
        self.assertEqual(auctions.status_code, 200)

    def test_create_auction(self):

        auction = {
            'description': 'test description',
            'end_time': '2020-09-10T00:00:00',
            'condition': 'Used'
        }
        mike = User.objects.get(username='mike')
        factory = APIRequestFactory()
        view = AuctionViewSet.as_view({'post': 'create'})
        req = factory.post('/api/auction/', data=auction)
        force_authenticate(req, user=mike, token=get_token(self.mike))
        res = view(req)

    def test_list_auction(self):
        mike = User.objects.get(username='mike')
        factory = APIRequestFactory()
        view = AuctionViewSet.as_view({'get': 'list'})
        req = factory.get('/api/auction/1')
        force_authenticate(req, user=mike, token=get_token(self.mike))
        res = view(req)

    def test_post_bid(self):
        bid = {
            'auction': '1',
            'amount': '10'
        }
        oli = User.objects.get(username='oli')
        mary = User.objects.get(username='mary')
        factory = APIRequestFactory()
        view = BidViewSet.as_view({'post': 'create'})
        req = factory.post('/api/auction/', data=bid)
        force_authenticate(req, user=oli, token=get_token(self.oli))
        res = view(req)

        bid["amount"] = '20'
        req = factory.post('/api/auction/', data=bid)
        force_authenticate(req, user=mary, token=get_token(self.mary))
        res = view(req)
