from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=160)
    def __str__(self):
        return self.name

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Meta:
    unique_together = ('user', 'topic',)


class Feedback(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    rating = models.IntegerField (validators=[
        MinValueValidator(0), MaxValueValidator(5)])
    good = models.TextField(max_length=2000, blank=True)
    bad = models.TextField(max_length=2000, blank=True)
    ideas = models.TextField(max_length=2000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.date}"
