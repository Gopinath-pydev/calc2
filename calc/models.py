from django.db import models
from datetime import datetime
from pytz import timezone


now_utc = datetime.now(timezone('UTC'))
class userProp(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_allowed = models.BooleanField(default=True)
    signed_at = models.DateTimeField(default=now_utc.astimezone(timezone('Asia/Kolkata')))
    # user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

