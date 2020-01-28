from django.db import models


class Chapter(models.Model):
    name = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(max_length=512)
    url = models.CharField(max_length=1024)
