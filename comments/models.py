from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from residences.models import Residence, Hotel
from tickets.models import AirplaneTicket

# -------------------------------------------------comment--------------------------------------------------------------
# Abstract Model--------------------------------------------------------------------------------------------------------
class AbstractComment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)ss')
    comment_body = models.TextField()

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Residence Comment-----------------------------------------------------------------------------------------------------
class ResidenceComment(AbstractComment):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='comments')


# Hotel Comment---------------------------------------------------------------------------------------------------------
class HotelComment(AbstractComment):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')


# AirPlane Ticket Comment-----------------------------------------------------------------------------------------------
class AirplaneTicketComment(AbstractComment):
    airplane_ticket = models.ForeignKey(AirplaneTicket, on_delete=models.CASCADE, related_name='comments')


# --------------------------------------------------rate----------------------------------------------------------------
# Abstract Model--------------------------------------------------------------------------------------------------------
class AbstractRating(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)ss')
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Residence Rating------------------------------------------------------------------------------------------------------
class ResidenceRating(AbstractRating):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='rates')

    class Meta:
        unique_together = ['user', 'residence']


# Hotel Rating----------------------------------------------------------------------------------------------------------
class HotelRating(AbstractRating):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rates')

    class Meta:
        unique_together = ['user', 'hotel']


# AirPlane Ticket Rating------------------------------------------------------------------------------------------------
class AirplaneTicketRating(AbstractRating):
    airplane_ticket = models.ForeignKey(AirplaneTicket, on_delete=models.CASCADE, related_name='rates')

    class Meta:
        unique_together = ['user', 'airplane_ticket']

