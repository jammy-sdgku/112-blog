from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
#status table
class Status(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description= models.CharField(max_length=256, help_text="Please describe the status")
    
    def __str__(self):
        return self.name

#post table
class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.TextField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status= models.ForeignKey(
        Status,
            on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title       
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
