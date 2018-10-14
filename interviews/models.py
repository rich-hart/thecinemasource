from django.db import models

class Photograph(models.Model):
     filename = models.CharField(max_length = 255)
     post_id = models.IntegerField()

