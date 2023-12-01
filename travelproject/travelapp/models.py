from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
class People(models.Model):
    names = models.CharField(max_length=250)
    imges = models.ImageField(upload_to='pic')
    descp = models.TextField()
    def __str__(self):
        return self.names



