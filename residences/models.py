from django.db import models
from django.conf import settings
from django.utils import timezone

now = timezone.localtime(timezone.now(), timezone.zoneinfo.ZoneInfo(key='Asia/Tehran'))


# Location-related models-----------------------------------------------------------------------------------------------
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


# Residences models-----------------------------------------------------------------------------------------------------
class AbstractResidence(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    capacity = models.PositiveSmallIntegerField(default=None, null=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Residence(AbstractResidence):
    city = models.ForeignKey(City, related_name='residences', on_delete=models.CASCADE, null=True, blank=True)
    bedroom = models.PositiveSmallIntegerField(default=0)
    bed = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title


class Hotel(AbstractResidence):
    city = models.ForeignKey(City, related_name='hotels', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Unit(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    capacity = models.PositiveSmallIntegerField(default=1)
    bedroom = models.PositiveSmallIntegerField(default=0)
    bed = models.PositiveSmallIntegerField(default=1)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='units', null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Price related model---------------------------------------------------------------------------------------------------
class PriceInfo(models.Model):
    currency = models.CharField(max_length=3, default='IRR')
    price = models.PositiveIntegerField(null=True, blank=True)
    weekday = models.PositiveSmallIntegerField(default=now.weekday())

    residence = models.OneToOneField(Residence, on_delete=models.CASCADE, related_name='price_info',
                                     null=True, blank=True)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='price_info', null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_price(self):
        weekend_ratio = 1.2
        weekend = [0, 1]
        if self.weekday in weekend:
            self.price *= weekend_ratio
        return self.price

    def __str__(self):
        return f'{self.price}_{self.currency}'


# Image-related models--------------------------------------------------------------------------------------------------
class ImageAlbum(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)

    residence = models.OneToOneField(Residence, on_delete=models.CASCADE, related_name='image_album',
                                     null=True, blank=True)
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, related_name='image_album', null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    avatar = models.ImageField(upload_to='residences/', null=True, blank=True)

    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Facility model--------------------------------------------------------------------------------------------------------
class Facility(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='facilities', null=True, blank=True)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='facilities', null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='facilities', null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "facilities"

    def __str__(self):
        return self.title


# Policy model----------------------------------------------------------------------------------------------------------
class Policy(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default=None)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='policies', null=True, blank=True)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='policies', null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "policies"

    def __str__(self):
        return self.title


# Rent_related models---------------------------------------------------------------------------------------------------
class RentResidence(models.Model):
    date = models.DateField(blank=True, default=now.date())
    residence = models.ForeignKey(Residence, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='rented_days')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name='rent_residence')

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('date', 'residence')

    def __str__(self):
        return f'{self.residence}-{self.date}'


class RentHotel(models.Model):
    date = models.DateField(blank=True, default=now.date())
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.CASCADE, related_name='rented_days')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name='rent_hotel')

    class Meta:
        unique_together = ('date', 'unit')

    def __str__(self):
        return f'{self.unit}-{self.date}'
