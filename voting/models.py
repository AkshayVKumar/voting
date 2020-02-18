from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Constituency(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Candidate(models.Model):
    name=models.CharField(max_length=50)
    constituency=models.ForeignKey(Constituency,on_delete=models.CASCADE)
    no_votes=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Voter(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_voted=models.BooleanField(default=False)
    constituency=models.ForeignKey(Constituency,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

