from django.urls import path

from . import views, models

urlpatterns = [
    path('', views.index, name="index"),
    path('api/v1/auction/<int:auctionID>', views.Auction.as_view()),
    path('api/v1/user/<int:userID>', views.User.as_view()),
]