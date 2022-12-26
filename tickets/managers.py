from django.db import models
from django.utils import timezone

# now = timezone.localtime(timezone.now(), timezone.zoneinfo.ZoneInfo(key='Asia/Tehran'))
# now = timezone.now()
now = timezone.localtime()


class ValidTickets(models.Manager):
    def get_queryset(self):
        return super(ValidTickets, self).get_queryset().filter(time__gte=now, capacity__gt=0)



