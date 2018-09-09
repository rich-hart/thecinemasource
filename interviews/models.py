from django.db import models


class Interview(models.Model):
    full_name = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()

class Photograph(models.Model):
    link = models.URLField()
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)


