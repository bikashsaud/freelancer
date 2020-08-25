from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    proficiency = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Language(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    language = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=32)

    def __str__(self):
        return self.language


