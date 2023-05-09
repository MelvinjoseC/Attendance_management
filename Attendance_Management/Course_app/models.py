from django.db import models

# Create your models here.

class  Qualifications_name(models.Model):
    Qualification_name = models.CharField(max_length=100)

class  Statename(models.Model):
    State_name = models.CharField(max_length=50)

    
