from django.db import models

# Create your models here.


class Students(models.Model):
    FirstName = models.CharField(unique=False, max_length=20)
    LastName = models.CharField(unique=False, max_length=20)
    Email = models.EmailField(unique=True)
    Password = models.CharField(unique=False, max_length=50)

    def __str__(self):
        return self.FirstName


