from django.db import models

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        return self.name 
         

class Track(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Session(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.title