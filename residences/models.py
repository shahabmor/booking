from django.db import models


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

# Price related model---------------------------------------------------------------------------------------------------


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


# Image-related models--------------------------------------------------------------------------------------------------
class ImageAlbum(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)

    residence = models.OneToOneField(Residence, on_delete=models.CASCADE, related_name='image_album', null=True, blank=True)
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


