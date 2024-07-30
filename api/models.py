from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def str(self):
        return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question,related_name='answer' ,on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Answer to {self.question.title} by {self.author.username}"

 
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Feedback from {self.name}"