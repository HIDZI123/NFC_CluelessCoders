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
    description = models.TextField(blank=True)
    symptoms = models.TextField()
    causes = models.TextField()
    prevention = models.TextField()
    remedies=models.TextField()
    drug=models.ForeignKey('Drug',on_delete=models.CASCADE,blank=True)
    clinic = models.URLField(max_length=200,blank=True)

    def __str__(self):
        return self.name    

    def formatted_symptoms(self):
        return self.format_text_field(self.symptoms)

    def formatted_causes(self):
        return self.format_text_field(self.causes)

    def formatted_prevention(self):
        return self.format_text_field(self.prevention)

    def formatted_remedies(self):
        return self.format_text_field(self.remedies)

    def format_text_field(self, field_text):
        return field_text.split('\n')

