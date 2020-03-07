from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Auction(models.Model):
    class conditions(models.TextChoices):
        NEW = 'New', ('New')
        USED = 'Used', ('Used')

    owner = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='owner')
    winner = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='winner', null=True)
    highest_bid = models.ForeignKey('Bid', on_delete=models.CASCADE,
        related_name='highest_bid', blank=True, null=True)
    highest_bid_amount = models.IntegerField(default=0, blank=True, null=True)
    description = models.CharField(max_length=255)
    end_time = models.DateTimeField('end date', default=now)
    active = models.BooleanField(default=True)
    time_created = models.DateTimeField('time created', default=now)
    condition = models.CharField(choices=conditions.choices, default=conditions.USED, max_length=4)

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



