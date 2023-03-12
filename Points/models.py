from django.db import models

class Post(models.Model):
    rp = models.IntegerField()
    mp = models.IntegerField()

    def __int__(self):
        return self.rp