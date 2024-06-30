
from django.db import models

class details(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    clgname = models.CharField(max_length=100)

    def __str__(self):
        return self.name