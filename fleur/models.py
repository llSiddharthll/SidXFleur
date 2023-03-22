from django.db import models

# Create your models here.

class Rom(models.Model):
    rom_name = models.CharField(max_length=50)
    rom_link = models.URLField(max_length=200,null=True, blank=True,unique=True)
    android = models.FloatField()
    version = models.DateField()
    bugs = models.CharField(max_length=100,null=True)
    credit = models.CharField(max_length=150,null=True)
    fw=models.CharField(max_length=50)
    boot=models.CharField(max_length=50)
    def __str__(self):
        return self.rom_name
    
class Mod(models.Model):
    mod_link = models.URLField(max_length=200, blank=True,unique=True)
    mod_name = models.CharField(max_length=50)
    mod_credits= models.CharField(max_length=150,null=True)
    mod_android = models.CharField(max_length=50)
    purpose = models.CharField(max_length=150,null=True)
    def __str__(self):
        if self.purpose==None and self.mod_credits==None:
            return "Data not provided !!"
        return self.mod_name
    
class Contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
    subject=models.CharField(max_length=100,null=True)
    message=models.TextField(null=True)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    name=models.CharField(max_length=50)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.name