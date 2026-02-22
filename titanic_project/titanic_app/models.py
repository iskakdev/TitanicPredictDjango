from django.db import models

class Titanic(models.Model):
    Pclass = models.IntegerField()
    Sex = models.CharField(max_length=32)
    Age = models.IntegerField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare = models.FloatField()
    SibParch = models.IntegerField()
    Embarked = models.CharField(max_length=32)
