from django.db import models
from profiles.models import UserProfile


# Create your models here.

class Debt(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='receiver', on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirm = models.BooleanField()
    last_update_timestamp = models.IntegerField(max_length=20, default=0)
    timestamp = models.IntegerField(max_length=30, primary_key=True)
    # pk = models.CharField(max_length=100) # sender + timestamp + receiver

    def __str__(self):
        return "%s %s %s %s" % (self.sender, self.receiver, self.count, self.is_confirm)
