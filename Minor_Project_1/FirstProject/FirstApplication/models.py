from django.db import models
# Create your models here.


class Candidates(models.Model):

    CandidateName = models.CharField(unique=False, max_length=30)
    CandidateId = models.CharField(max_length=20)  # There might be different person with same name,
    ContactNum = models.CharField(max_length=20)                                                             # that is why we ave given unique = False.
    Address = models.CharField(max_length=20)
