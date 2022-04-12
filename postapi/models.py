from email import message
from django.db import models

# Create your models here.
class Fields(models.Model):
    name = models.CharField(max_length=100, blank = False, null= False)
    email = models.EmailField(max_length=50, blank = False)
    message = models.TextField(max_length=400, blank =False)

    def __str__(self):
        return f'{self.name} ({self.email})'
        
    