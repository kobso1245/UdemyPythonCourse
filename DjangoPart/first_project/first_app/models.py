from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, models.SET_NULL, null=True)
    date = models.DateField()