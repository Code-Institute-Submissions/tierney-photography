from django.db import models
from django.contrib.auth.models import User
from shop.models import PhotoSet


class Order(models.Model):
    """ Model for user data to be entered into when making an order """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    address1 = models.CharField(max_length=60, blank=False)
    address2 = models.CharField(max_length=60, blank=False)
    city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.first_name, self.last_name)


class OrderLineItem(models.Model):
    """ Model for title and price of each line of the order """
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    photoset = models.ForeignKey(PhotoSet, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} @ {1}".format(self.photoset.title, self.photoset.price)
