from django.db import models

# Create your models here.

class Demo(models.Model):
    post = models.TextField()
    
    def __str__(self):
        return self.post