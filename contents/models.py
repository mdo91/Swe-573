from django.db import models
from lessons.models import Lessons
from django.utils.datastructures import MultiValueDictKeyError
class Contents(models.Model):
    material_title = models.TextField()
    content = models.TextField()
    lessonId = models.ForeignKey(Lessons,on_delete = models.CASCADE)
