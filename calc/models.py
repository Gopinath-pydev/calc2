from django.db import models
import timezone

class userProp(models.Model):
    name = models.CharField(max_Length=100)
    age = models.IntegerField()
    is_allowed = models.BooleanField(default=True)
    signed_at = models.DateTimeField(default=timezone.now())

