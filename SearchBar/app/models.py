from django.db import models

# Create your models here.
class Data(models.Model):
    firse_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.firse_name
