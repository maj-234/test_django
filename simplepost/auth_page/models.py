from django.db import models

# Create your models here.

class Blog(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)
    create_time = models.DateTimeField(auto_now_add=True)
    