from django.conf import settings
from django.db import models


class AbstractComment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)ss')
    comment_body = models.TextField()

    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

