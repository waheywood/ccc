from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from .serializers import CreateUserSerializer


CLIENT_ID = 'YxFwIXmjNIbGzN9z3HqABQIVK7wNQxAvxXUPAwQo'
CLIENT_SECRET = '4eWJ6XbnXlr0pJCYnwTWKtNc6nWLY1J4dJvVQzFgCvjCnMv4Hjgd7JVQJexLR8IowGowCPiFyBiVFNQTirTTPkWGrQUaJQQMZeFClTd882yQ7rujq3hC45MyaU0NE9dT'
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serial = CreateUserSerializer(data=request.data)
    if serial.is_valid():
        serial.save()

        req = requests.post('http://localhost:8000/oauth/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            })
        return Response(req.json())
    return Response(serial.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    req = requests.post(
        'http://localhost:8000/oauth/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
    })
    return Response(req.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    req = requests.post(
    'http://localhost:8000/oauth/token/', 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })
    return Response(req.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    req = requests.post(
        'http://localhost:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if req.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, req.status_code)

    return Response(req.json(), req.status_code)


