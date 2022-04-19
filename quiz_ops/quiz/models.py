from django.db import models

# Create your models here.
class Question(models.Model):
    text=models.CharField(max_length=2500, null=True, blank=True)
    marks=models.IntegerField(null=True, blank=True)
    explanation=models.CharField(max_length=5000,null=True,blank=True)
    active=models.BooleanField(default=True)
    weight=models.IntegerField(null=True, blank=True)

class Options(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE, null=True, blank=True)
    option_text=models.CharField(max_length=1000,null=True,blank=True)
    option_flag=models.BooleanField(default=False)
    option_status=models.BooleanField(default=True)
