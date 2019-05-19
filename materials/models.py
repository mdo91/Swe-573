from django.db import models
from courses.models import Courses
from lessons.models import Lessons
from django.utils.datastructures import MultiValueDictKeyError
class Materials(models.Model):
    material_title = models.TextField()
    content = models.TextField()
    lesson_id = models.ForeignKey(Lessons,on_delete= models.CASCADE)


# Create your models here.
