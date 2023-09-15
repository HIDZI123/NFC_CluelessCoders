from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ayurveda(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Drug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name    


class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    drug = models.ForeignKey("Drug", on_delete=models.CASCADE)
    ayurveda = models.ForeignKey("Ayurveda", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    



class Part(models.Model):
    name=models.CharField(max_length=100)
    disease=models.ManyToManyField(Disease,blank=True,related_name='part')

    
    def __str__(self):
        return self.name    
