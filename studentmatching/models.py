from django.db import models

# Create your models here.
class Organization(models.Model):
    org_text = models.CharField(max_length=50)

class classes(models.Model):
    class_text = models.CharField(max_length=50)

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    classes= models.ForeignKey(classes,on_delete=models.CASCADE)
    organizations=models.ForeignKey(Organization,on_delete=models.CASCADE)





