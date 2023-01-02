from django.db import models
from django.utils import timezone
from django.conf import settings


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

    city = models.ForeignKey(City, related_name='%(class)ss', on_delete=models.CASCADE, null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Residence(AbstractResidence):
    bedroom = models.PositiveSmallIntegerField(default=0)
    bed = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title


class Hotel(AbstractResidence):
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

class Currency(models.Model):
    title = models.CharField(max_length=3, default='IRR')

class AbstractPriceInfo(models.Model):
    price = models.PositiveIntegerField(null=True, blank=True)
    currency = models.ForeignKey(Currency, related_name='%(class)ss', on_delete=models.CASCADE)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_price(self, date=timezone.now(), weekend=(2, 3), weekend_ratio=1.2, holiday=(), holiday_ratio=1):
        price = self.price

        """
        :param date:
        :param weekend:
        :param weekend_ratio:
        :param holiday:
        :param holiday_ratio:
        :return:
        """

        weekday = date.weekday()
        if weekday in weekend:
            price *= weekend_ratio

        if date in holiday:
            price *= holiday_ratio

        return round(price)
        # try:
        #     return round(price)
        # except TypeError:
        #     return self.price

    def __str__(self):
        return f'{self.price}_{self.currency}'


class CurrencyExchangeRate(models.Model):

    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_from')
    currency_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_to')

    rate = models.FloatField()

class ResidencePriceInfo(AbstractPriceInfo):
    residence = models.OneToOneField(Residence, on_delete=models.CASCADE, related_name='price_info',
                                     null=True, blank=True)

class UnitPriceInfo(AbstractPriceInfo):
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='price_info', null=True, blank=True)


# Image-related models--------------------------------------------------------------------------------------------------
class AbstractImage(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)

    avatar = models.ImageField(upload_to='%(class)ss', null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ResidenceImage(AbstractImage):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='image_album',
                                  null=True, blank=True)

class HotelImage(AbstractImage):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='image_album', null=True, blank=True)


# Facility model--------------------------------------------------------------------------------------------------------
class AbstractFacility(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class ResidenceFacility(AbstractFacility):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='facilities', null=True, blank=True)

    class Meta:
        verbose_name_plural = "residence_facilities"


class HotelFacility(AbstractFacility):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='facilities', null=True, blank=True)

    class Meta:
        verbose_name_plural = "hotel_facilities"

class UnitFacility(AbstractFacility):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='facilities', null=True, blank=True)

    class Meta:
        verbose_name_plural = "unit_facilities"


# Policy model----------------------------------------------------------------------------------------------------------
class AbstractPolicy(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default=None)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class ResidencePolicy(AbstractPolicy):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='policies', null=True, blank=True)

    class Meta:
        verbose_name_plural = "residence_policies"


class HotelPolicy(AbstractPolicy):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='policies', null=True, blank=True)

    class Meta:
        verbose_name_plural = "hotel_policies"

# Rent_related models---------------------------------------------------------------------------------------------------
class RentResidence(models.Model):
    date = models.DateField(blank=True, null=True)
    # date = models.DateField(default=timezone.now().date())
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
    date = models.DateField(blank=True, null=True)
    # date = models.DateField(default=timezone.now().date())
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.CASCADE, related_name='rented_days')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name='rent_hotel')

    class Meta:
        unique_together = ('date', 'unit')

    def __str__(self):
        return f'{self.unit}-{self.date}'


