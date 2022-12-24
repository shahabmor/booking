from django.db import models

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

    time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    duration = models.TimeField(null=True, blank=True)

    origin = models.ForeignKey(Terminal, related_name='%(class)ss_departure', on_delete=models.CASCADE, null=True, blank=True)
    destination = models.ForeignKey(Terminal, related_name='%(class)ss_arrival', on_delete=models.CASCADE,
                                    null=True, blank=True)

    capacity = models.PositiveSmallIntegerField(default=1)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AirplaneTicket(AbstractTicket):
    airplane = models.CharField(max_length=100, null=True, blank=True)
    flight_number = models.PositiveSmallIntegerField(null=True, blank=True)
    terminal = models.PositiveSmallIntegerField(null=True, blank=True)


# Facility model--------------------------------------------------------------------------------------------------------
class Facility(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)

    airplane_ticket = models.ForeignKey(AirplaneTicket, related_name='facilities', on_delete=models.CASCADE,
                                        null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "facilities"

    def __str__(self):
        return self.title
#

# Policy model--------------------------------------------------------------------------------------------------------
class Policy(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)

    airplane_ticket = models.ForeignKey(AirplaneTicket, related_name='policies', on_delete=models.CASCADE,
                                        null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "policies"

    def __str__(self):
        return self.title


# Price model-----------------------------------------------------------------------------------------------------------
class PriceInfo(models.Model):
    currency = models.CharField(max_length=3, default='IRR')
    price = models.PositiveIntegerField(null=True, blank=True)

    airplane_ticket = models.ForeignKey(AirplaneTicket, related_name='price_info', on_delete=models.CASCADE,
                                        null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.price}_{self.currency}'



