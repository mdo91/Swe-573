from django.db import models
from contents.models import Contents
from django.utils.datastructures import MultiValueDictKeyError
class Questions(models.Model):
    question_text = models.TextField()
    materialId = models.ForeignKey(Contents,on_delete=models.CASCADE)
