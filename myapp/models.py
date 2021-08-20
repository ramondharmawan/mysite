from django.db import models

# Create your models here.
# create class and name the model Link


class Link(models.Model):
    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
