from django.db import models
from django.conf import settings
from django.db.models import Avg

from .managers import ValidTickets
from residences.models import AbstractFacility, AbstractPolicy, AbstractPriceInfo

from rest_framework import validators
from django.utils import timezone

# Terminal-related models-----------------------------------------------------------------------------------------------
class Country(models.Model):
    title = models.CharField(max_length=100)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.title

class City(models.Model):
    title = models.CharField(max_length=100)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.title


class Terminal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    city = models.ForeignKey(City, related_name='terminals', on_delete=models.CASCADE, null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Ticket models---------------------------------------------------------------------------------------------------------
class AbstractTicket(models.Model):
    company = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    time = models.DateTimeField(null=True, blank=True)

    duration = models.TimeField(null=True, blank=True)

    origin = models.ForeignKey(Terminal, related_name='%(class)ss_departure', on_delete=models.CASCADE,
                               null=True, blank=True)
    destination = models.ForeignKey(Terminal, related_name='%(class)ss_arrival', on_delete=models.CASCADE,
                                    null=True, blank=True)

    capacity = models.PositiveSmallIntegerField(default=1)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    valid_tickets = ValidTickets()

    class Meta:
        abstract = True


class AirplaneTicket(AbstractTicket):
    airplane = models.CharField(max_length=100, null=True, blank=True)
    flight_number = models.PositiveSmallIntegerField(null=True, blank=True)
    terminal = models.PositiveSmallIntegerField(null=True, blank=True)

    @property
    def average_rating(self):
        rate = self.rates.all().aggregate(avg=Avg('rate'))
        return rate.get('avg') or '-.-'


# Facility model--------------------------------------------------------------------------------------------------------
class AirPlaneTicketFacility(AbstractFacility):
    airplane_ticket = models.ForeignKey(AirplaneTicket, related_name='facilities', on_delete=models.CASCADE,
                                        null=True, blank=True)


# Policy model----------------------------------------------------------------------------------------------------------
class AirPlaneTicketPolicy(AbstractPolicy):
    airplane_ticket = models.ForeignKey(AirplaneTicket, related_name='policies', on_delete=models.CASCADE,
                                        null=True, blank=True)

# Price model-----------------------------------------------------------------------------------------------------------
class AirPlaneTicketPriceInfo(AbstractPriceInfo):
    airplane_ticket = models.OneToOneField(AirplaneTicket, related_name='price_info', on_delete=models.CASCADE,
                                           null=True, blank=True)


# Buy-related models----------------------------------------------------------------------------------------------------
class BuyAirPlaneTicket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name='airplane_tickets')
    ticket = models.ForeignKey(AirplaneTicket, blank=True, null=True, on_delete=models.CASCADE,
                               related_name='sold_tickets')
    count = models.PositiveSmallIntegerField(default=1)






