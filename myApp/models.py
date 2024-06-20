from django.db import models

# Create your models here.

class information(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstname
