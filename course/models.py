from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=150,primary_key=False,default="",null=True)
    description = models.TextField(max_length=300,primary_key=False,default="")


    def __str__(self):
        return self.title

class Chapter(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=100,default="Title")
    content = models.TextField(max_length=10000,default="Content")
    chapter_covers = models.CharField(max_length=50,default="Chapter covers:")
    summary = models.CharField(max_length=500,default="Chapter Summary:")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# I want a variable that changes based on every single user. I want this variable to be automatically created for every chapter

class ImportantInstructionContent(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default="")
    important_content = models.TextField(max_length=100,default="")
    def __str(self):
        return self.important_content



class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, default="")
    question_text = models.CharField(max_length=200,default="Let's Write Your First Program!")
    pub_date = models.DateTimeField("date published")
    explanation = models.TextField(default="Explanation")
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    correct_choice = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text
