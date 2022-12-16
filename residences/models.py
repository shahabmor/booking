from django.db import models

# Policy model
class Policy(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default=None)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title


# Facility model
class Facility(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title


# Image-related models
class ImageAlbum(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class Image(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    avatar = models.ImageField(upload_to='residences/', null=True, blank=True)

    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


# Unit model
class Unit(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    capacity = models.PositiveSmallIntegerField(default=1)
    bedroom = models.PositiveSmallIntegerField(default=0)
    bed = models.PositiveSmallIntegerField(default=1)
    image_album = models.OneToOneField(ImageAlbum, related_name='unit', on_delete=models.CASCADE)

    facilities = models.ManyToManyField(Facility, related_name='units', default=None)
    policies = models.ManyToManyField(Policy, related_name='units', default=None)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title


# Location-related models
class Country(models.Model):
    title = models.CharField(max_length=100)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=100)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    def get_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title


# Residences models
# Hotel model
class Hotel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    capacity = models.PositiveSmallIntegerField(default=None, null=True)
    image_album = models.OneToOneField(ImageAlbum, related_name='hotel', on_delete=models.CASCADE)

    units = models.ManyToManyField(Unit, related_name='hotels', default=None)
    facilities = models.ManyToManyField(Facility, related_name='hotels', default=None)
    policies = models.ManyToManyField(Policy, related_name='hotels', default=None)

    city = models.ForeignKey(City, related_name='hotels', default=None, null=True, on_delete=models.CASCADE)

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title


# Residence model
class Residence(Unit):
    city = models.ForeignKey(City, related_name='residences', default=None, null=True, on_delete=models.CASCADE)
