from django.db import models

# Create your models here.
class Question(models.Model):
      title = models.CharField()
      author = models.CharField()
      createdate = models.DateField()



class Answers(models.Model):
      question = models.CharField()
      author = models.CharField()
      answer = models.CharField()
      createdate = models.DateField()
      