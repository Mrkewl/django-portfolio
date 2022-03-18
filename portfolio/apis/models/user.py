from django.db import models



class User(models.Model):
    name=models.CharField(max_length=20)
    occupation=models.CharField(max_length=100)
    age=models.IntegerField()
    stack=models.TextField()
    about_me=models.TextField()
    profile_picture_url=models.TextField()

