from django.db import models

# Create your models here.
class member(models.Model):
    memberId = models.IntegerField
    email = models.CharField(max_length = 255)
class otp(models.Model):
    member = models.ForeignKey(member, on_delete=models.CASCADE)
    otp = models.IntegerField
    generatedOn = models.DateField