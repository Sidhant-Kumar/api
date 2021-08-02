from django.db import models


# Create your models here.
class apimodel(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name
