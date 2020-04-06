from django.db import models

# Create your models here.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Guide(models.Model):
    name = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100)    


    def __str__(self):
        return self.namei, self.major

class Visitor(models.Model):

    name = models.CharField(max_length = 100)
    visit_date = models.DateTimeField('date of visit')







