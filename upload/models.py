from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
