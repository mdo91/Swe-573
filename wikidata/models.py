from django.db import models
from courses.models import Courses
# Create your models here.
class Wikidata(models.Model):
    wikiTitle = models.CharField(max_length=255)
    wikiLink  = models.TextField()
    topic_id  = models.ForeignKey(Courses,on_delete=models.CASCADE)
