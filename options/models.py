from django.db import models
from questions.models import Questions
from django.utils.datastructures import MultiValueDictKeyError
class Options(models.Model):
    optionText = models.TextField()
    answer = models.BooleanField(default=False)
    questionId = models.ForeignKey(Questions,on_delete=models.CASCADE)
# Create your models here.
