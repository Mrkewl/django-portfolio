from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    key_contribtion = models.TextField()
    logo_url = models.TextField(default='https://media.gaigai.com/2020/09/71103625-gaigai_weblogo_500pxw.png')
    created = models.DateField()
    updated = models.DateField()
    google_app_link = models.TextField()
    apple_app_link = models.TextField()
    picture_url = models.TextField()
    hello = models.TextField()