from django.db import models

# Create your models here.

class Signup(models.Model):
    uname = models.CharField(max_length=100)
    uphone = models.CharField(max_length=15)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=True,null=True)  

    def __str__(self):
        return f'{self.username} {self.email}'


class AdminLogin(models.Model):
    ausername = models.CharField(max_length=100, unique=True)
    apassword = models.CharField(max_length=100)

    def __str__(self):
        return self.ausername

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
