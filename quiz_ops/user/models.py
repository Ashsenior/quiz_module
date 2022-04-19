from django.db import models
from quiz.models import *
# Create your models here.
class UserQuizSummary(models.Model):
    user = models.CharField(max_length=100,null=True,blank=True)
    quiz_name=models.CharField(max_length=100,null=True,blank=True)
    quiz_date=models.DateField(null=True,blank=True)
    no_correct_attempt=models.IntegerField(null=True,blank=True,default=0)
    no_wrong_attempt=models.IntegerField(null=True,blank=True,default=0)


class UserQuizDetail(models.Model):
    quiz_id=models.ForeignKey(UserQuizSummary,on_delete=models.CASCADE,null=True,blank=True)
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
    user_answer=models.IntegerField(null=True, blank=True)
