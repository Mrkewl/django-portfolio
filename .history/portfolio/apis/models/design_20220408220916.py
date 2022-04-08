from django.db import models
from django.contrib.postgres.fields import ArrayField

class Design(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.TextField()
    description = models.TextField()
    theme = models.CharField(max_length=30)
    screens_urls = ArrayField(
        models.TextField()
    )
