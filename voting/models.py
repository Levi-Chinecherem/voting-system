from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class VotingPosition(models.Model):
    position = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.position

    def is_active(self):
        now = datetime.now()
        return self.start_date <= now <= self.end_date

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(VotingPosition, on_delete=models.CASCADE)
    details = models.TextField()
    image = models.ImageField(upload_to='candidates')

    def __str__(self):
        return self.name

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"
