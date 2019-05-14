from django.db import models
from courses.models import Courses
from django.utils.datastructures import MultiValueDictKeyError
# class Courses(models.Model):
class Lessons(models.Model):
    lesson_title = models.CharField(max_length=255)
    lesson_hierarchy = models.IntegerField()
    topic_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    # country = models.ForeignKey('Country',null=False)

# Create your models here.
