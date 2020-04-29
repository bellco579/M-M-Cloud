from django.db import models

# Create your models here.


class UserProfile(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "%s" % self.uid
