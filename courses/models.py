from django.db import models
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

# Create your models here.
class Courses(models.Model):
    topicTitle = models.CharField(max_length=255)
    description =  models.TextField()
    userId = models.ForeignKey(User,on_delete = models.CASCADE)
    
