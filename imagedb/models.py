from django.db import models

# Create your models here.
class Album(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField(blank=True)

  def __str__(self):
    return self.name


class Image(models.Model):
  url = models.CharField(max_length=255)
  time = models.DateField()
  desc = models.TextField()
  tags = models.CharField(max_length=255)
  album = models.ForeignKey(Album)


class Upload(models.Model):
  tags = models.CharField(max_length=255)
  file = models.FileField()
  album = models.ForeignKey(Album)
  
